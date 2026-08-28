# PostgreSQL FastAPI CRUD

A small CRUD API backed by PostgreSQL and run with Docker Compose.

## Prerequisites

- Docker Desktop with Docker Compose

## Run the application

Build and start the services in the background:

```bash
docker compose up -d --build
```

The API is available at <http://localhost:8080>.

## Development

The development Compose file mounts the API source and enables FastAPI's auto-reload server:

```bash
docker compose -f compose.yml -f compose-dev.yml up --build
```

See the [API README](api/README.md) for endpoints, documentation, and request examples.

## Stop the application

```bash
docker compose down
```

See the [database README](db/README.md) for PostgreSQL configuration and initialisation details.