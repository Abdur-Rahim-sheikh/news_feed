from django.http import JsonResponse
from django.views import View

from ..data import SourceRepository
from ..schemas import Source


class SourceView(View):
    def __init__(self):
        self._repository = SourceRepository()

    def get(self, request):
        sources = self._repository.get_all()
        return JsonResponse(data={"sources": self.format_sources(sources)}, status=200)

    def format_sources(self, sources: list[Source]) -> list[dict]:
        return [{"id": source.id, "name": source.name} for source in sources]
