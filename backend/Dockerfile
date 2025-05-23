FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend

RUN uv sync --locked

COPY . .

CMD ["uv","run", "manage.py", "runserver"]