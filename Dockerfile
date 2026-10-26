FROM node:24-alpine AS frontend_build

RUN npm install --global bun@1.3.11

WORKDIR /app

COPY frontend/package.json frontend/bun.lock ./

RUN bun install --frozen-lockfile

COPY frontend/ .

RUN bun run typecheck && bun run build

FROM python:3.14-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /uvx /bin/

WORKDIR /app

COPY backend/ ./
COPY --from=frontend_build /app/build/client ./build/client

ENV UV_NO_DEV=1
ENV INSIDE_DOCKER=1
ENV PYTHONUNBUFFERED=1

RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
