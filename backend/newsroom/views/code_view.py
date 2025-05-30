import pycountry
from django.http import JsonResponse
from django.views import View

from ..data import SourceRepository
from ..schemas import Source


class CodeView(View):
    def __init__(self):
        self._repository = SourceRepository()

    def get(self, request):
        sources = self._repository.get_all()
        return JsonResponse(data=self.format_sources(sources), status=200)

    def format_sources(self, sources: list[Source]) -> list[dict]:
        sources_formated = [
            {"id": source.id, "name": source.name} for source in sources
        ]

        countries = [
            {
                "id": source.country_code,
                "name": pycountry.countries.get(alpha_2=source.country_code).name,
            }
            for source in sources
            if pycountry.countries.get(alpha_2=source.country_code)
        ]
        countries = []
        taken = set()
        for source in sources:
            code = source.country_code
            country = pycountry.countries.get(alpha_2=code)
            if not country or code in taken:
                continue
            countries.append({"id": code, "name": country.name})
            taken.add(source.country_code)
        return {"sources": sources_formated, "countries": countries}
