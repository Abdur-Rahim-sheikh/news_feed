import json
import logging

from django.db import IntegrityError
from django.http import JsonResponse
from django.views import View

from ..data import UserRepository
from ..schemas import User
from ..utils import UserForm, jwt_required

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserView(View):
    def __init__(self):
        super().__init__()
        self.__repository = UserRepository()

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse(
                data={"message": "invalid request payload", "error": e}, status=400
            )
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")
        username = data.get("username", "")
        email = data.get("email", "")
        password = data.get("password", "")
        form = UserForm(
            data={
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "password": password,
            }
        )
        if not form.is_valid():
            logger.error(f"Form data is not valid: {form.errors}")
            return JsonResponse(data={"error": "Form data is not valid"}, status=400)
        # validate form
        logger.info(f"{first_name=},{last_name=},{username},{email=}, {password=}")
        try:
            user = self.__repository.add_user(
                first_name, last_name, username, email, password
            )
        except IntegrityError:
            return JsonResponse(data={"error": "username or email exists"}, status=409)

        return JsonResponse(data=self.format_user(user), status=200)

    @jwt_required
    def put(self, request):
        user_id = request.user_id
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse(
                data={"message": "invalid request payload", "error": e}, status=400
            )
        country_codes = data.get("country_codes", [])
        source_ids = data.get("source_ids", [])
        keywords = data.get("keywords", [])
        logger.info(f"{country_codes=},{source_ids=}, {keywords=}")
        success = self.__repository.update_preference(
            user_id, country_codes, source_ids, keywords
        )

        if not success:
            return JsonResponse(
                data={"message": "user preference could not be updated"}, status=409
            )

        return JsonResponse(status=200, data={"message": "successfully updated"})

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
