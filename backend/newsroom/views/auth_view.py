import json
from datetime import datetime, timedelta, timezone

import jwt
from django.http import JsonResponse
from django.views import View
from environs import Env

from ..data import UserRepository
from ..schemas import User

env = Env()
env.read_env()


class AuthView(View):
    def __init__(self):
        super().__init__()
        self._secret_key = env.str("JWT_SECRET")
        self.__repository = UserRepository()

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse(
                data={"message": "Invalid request payload", "error": str(e)}, status=400
            )
        unifier: str = data.get("unifier", "")
        password = data.get("password", "")
        if unifier.endswith(".com") and "@" in unifier:
            user = self.__repository.get_user(email=unifier)
        else:
            user = self.__repository.get_user(username=unifier)
        if not user:
            return JsonResponse(
                data={"error": "User / password does not match"}, status=404
            )

        if not user.verify_password(password):
            return JsonResponse(
                data={"error": "User / password does not match"}, status=404
            )
        payload = {
            "id": user.id,
            "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=100),
            "iat": datetime.now(),
        }
        token = jwt.encode(
            payload=payload, key=self._secret_key, algorithm=env.str("JWT_ALGORITHM")
        )

        return JsonResponse(data=self.format_user(user, token), status=200)

    def format_user(self, user: User, token: str):
        return {
            "auth_token": token,
            "user": {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "country_codes": user.country_codes,
                "source_ids": user.source_ids,
                "keywords": user.keywords,
            },
        }
