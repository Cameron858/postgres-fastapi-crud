FROM python:3.13-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.7.8 /uv /uvx /bin/

COPY . /app
ENV UV_NO_DEV=1

WORKDIR /app
RUN uv sync --locked

CMD ["uv", "run", "python", "main.py"]