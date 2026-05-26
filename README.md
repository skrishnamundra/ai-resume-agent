# AI Resume Screening Agent

## Features
- Upload resumes (PDF/DOCX)
- Extract resume text
- Generate embeddings
- Store vectors in ChromaDB
- Match candidates with job descriptions
- AI-generated ranking summaries

## Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env`:

```env
OPENAI_API_KEY=your_api_key
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend:
http://localhost:8000

Docs:
http://localhost:8000/docs

## Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend:
http://localhost:3000

## Docker Setup

```bash
docker-compose up --build
```
