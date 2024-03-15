Backend (FastAPI)

Setup

- Python 3.10+
- Install deps: `pip install -r requirements.txt`
- Run: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

Endpoints

- `GET /health` — health check
- `POST /api/analyze/misinformation` — simple heuristic score and verdict
- `POST /api/moderation/bias` — heuristic bias labels and score
- `POST /api/debate/structure` — mock multi‑agent debate outputs


