# CLAUDE.md — YT Comment Analyzer

## Project Overview

Monorepo: React (Vite) frontend + Python Flask backend that fetches YouTube comments, runs VADER sentiment analysis, and queries GPT-3.5-turbo for contextual insights.

## Structure

```
client/   — React 18 + Vite frontend
server/   — Python 3 Flask backend
```

## Commands

### Frontend (`client/`)
```bash
npm install          # install dependencies
npm run dev          # dev server on http://localhost:5173
npm run build        # production build → dist/
npm run preview      # preview build on port 8080
npm run lint         # ESLint
```

### Backend (`server/`)
```bash
pip install -r requirements.txt   # install dependencies
python3 app.py                    # dev server on http://localhost:5000
```

### Docker
Each directory (`client/`, `server/`) has its own `Dockerfile`. Deployment target is Google Cloud Run.

## Environment Variables

Create `server/.env`:
```
YT_API_KEY=...
OPENAI_API_KEY=...
```

Never commit `.env` files.

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | React 18, Vite, Bootstrap 5, react-bootstrap, Recharts, Axios |
| Backend | Flask 3, Flask-CORS, Gunicorn |
| AI/ML | OpenAI `gpt-3.5-turbo`, VADER Sentiment |
| External APIs | YouTube Data API v3, quickchart.io (wordcloud) |
| Deployment | Docker, Google Cloud Run |

## Backend Architecture

`POST /analyze_video` pipeline:

1. **process_comments.py** — fetch up to 1,500 comments via YouTube API, sort by likes
2. **models_analysis.py** — VADER sentiment scoring weighted by normalized like counts
3. **gpt_analysis.py** — send top 20 comments to GPT-3.5-turbo
4. **wordcloud.py** — build wordcloud URL via quickchart.io

## Frontend Components

- `App.jsx` — main state & API call
- `SentimentChart.jsx` — Recharts pie/bar chart
- `AIResponse.jsx` — GPT response display
- `HighlightedComments.jsx` — top/bottom comments
- `Description.jsx`, `ImageComponent.jsx`, `ErrorYT.jsx` — supporting UI

## Tests

No test suite exists. If adding tests: use `pytest` for Python, `vitest` for React.

## MCP — context7

Używaj context7 do pobierania aktualnej dokumentacji bibliotek (React, Flask, Recharts, Axios, Vite, OpenAI SDK itp.).

1. `resolve-library-id(nazwa)` → znajdź ID biblioteki
2. `query-docs(id, topic)` → pobierz dokumentację

## Notes

- Cold-start optimization: frontend pings backend on first load to warm the Cloud Run container.
- CORS is globally enabled via `Flask-CORS` — tighten origins before any production changes.
- No existing CI/CD pipeline.
