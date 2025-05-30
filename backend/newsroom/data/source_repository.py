from ..models import Source as sourcedb
from ..schemas import Source


class SourceRepository:
    def get_all(self) -> list[Source]:
        data = sourcedb.objects.all()
        sources = []
        for row in data:
            source = Source(
                id=row.id,
                name=row.name,
                url=row.url,
                language_code=row.language_code,
                country_code=row.country_code,
            )
            sources.append(source)
        return sources
