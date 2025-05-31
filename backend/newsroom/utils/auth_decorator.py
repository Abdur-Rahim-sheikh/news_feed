from functools import wraps

import jwt
from django.http import JsonResponse
from environs import Env

from ..models import User

env = Env()
env.read_env()


def jwt_required(view_func):
    @wraps(view_func)
    def _wrap_view(_cls, request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Unauthorized Bearer"}, status=401)

        token = auth_header.split(" ")[-1]

        try:
            payload = jwt.decode(
                token, env.str("JWT_SECRET"), algorithms=[env.str("JWT_ALGORITHM")]
            )
            request.user_id = payload["id"]
        except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist) as e:
            return JsonResponse({"error": f"Unauthorized decode {e}"}, status=401)

        return view_func(_cls, request, *args, **kwargs)

    return _wrap_view
