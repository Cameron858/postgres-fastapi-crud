# Database

The application uses PostgreSQL through the `db` service defined in the root Compose file.

## Configuration

Copy the example environment file to `.env`, then set the PostgreSQL password:

```bash
cp example.env .env
```

Edit `.env` and replace the placeholder value with your password:

```env
POSTGRES_PASSWORD=your-secure-password
```

The `.env` file is used by Docker Compose when starting PostgreSQL. Keep local secrets out of version control when using this project outside development.

## Initialisation

PostgreSQL runs the SQL files in `init/` the first time the data volume is created:

- `001_schema.sql` creates the `list` table.
- `002_seed.sql` inserts example items.

To recreate the database and run the initialization scripts again, remove the existing volume:

```bash
docker compose down -v
docker compose up -d --build
```
