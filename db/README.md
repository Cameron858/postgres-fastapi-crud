# Database

The application uses PostgreSQL through the `db` service defined in the root Compose file.

## Initialisation

PostgreSQL runs the SQL files in `init/` the first time the data volume is created:

- `001_schema.sql` creates the `list` table.
- `002_seed.sql` inserts example items.

To recreate the database and run the initialisation scripts again, remove the existing volume:

```bash
docker compose down -v
docker compose up -d --build
```
