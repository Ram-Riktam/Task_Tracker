# Backend (aiohttp + SQLAlchemy async + SQLite)

This is a clean backend compatible with your Svelte frontend.

## Quick start

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

The API runs at http://0.0.0.0:8000

### Endpoints
- GET    /cards
- POST   /cards
- PUT    /cards/{id}
- DELETE /cards/{id}

### Notes
- IDs are UUID strings (not integers).
- If you previously had a different schema, consider deleting `cards.db` to let the app recreate it:
  ```bash
  rm -f cards.db
  ```
  (or migrate your data).
- CORS is enabled for `http://localhost:5173` and `http://127.0.0.1:5173` by default.