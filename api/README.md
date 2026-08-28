# API

The FastAPI service exposes CRUD operations for items stored in PostgreSQL.

The API is available at <http://localhost:8080> when the application is running.

## Endpoints

- `GET /health` - Check API health
- `GET /items/` - List all items
- `POST /items/` - Create an item
- `PUT /items/{id}?new_content=...` - Update an item
- `DELETE /items/{id}` - Delete an item

Interactive API documentation is available at <http://localhost:8080/docs>.

## Request examples

```bash
curl http://localhost:8080/health
curl http://localhost:8080/items/
curl -X POST http://localhost:8080/items/ \
	-H "Content-Type: application/json" \
	-d '{"content":"Read a book."}'
curl -X PUT "http://localhost:8080/items/1?new_content=Read%20two%20books."
curl -X DELETE http://localhost:8080/items/1
```
