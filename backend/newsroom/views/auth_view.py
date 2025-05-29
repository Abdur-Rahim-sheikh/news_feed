from django.http import JsonResponse
from django.views import View
from ..data import UserRepository
from ..schemas import User
import json


class AuthView(View):
    def __init__(self):
        super().__init__()
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
        return JsonResponse(data=self.format_user(user), status=200)

    def format_user(self, user: User):
        return {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "country_codes": user.country_codes,
            "source_ids": user.source_ids,
            "keywords": user.keywords,
        }
