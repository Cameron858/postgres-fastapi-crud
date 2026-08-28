# PostgreSQL FastAPI CRUD

A small CRUD API backed by PostgreSQL and run with Docker Compose.

## Prerequisites

- Docker Desktop with Docker Compose

## Configuration

Copy the example environment file to the project root as `.env`, then set the PostgreSQL values:

```bash
cp example.env .env
```

Edit `.env` and set `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `POSTGRES_HOST`, and `POSTGRES_PORT`. Docker Compose passes these shared variables to the database and API services.

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