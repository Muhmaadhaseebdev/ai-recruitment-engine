# AI Recruitment Workflow Engine — Matching API Starter

A FastAPI candidate-to-role matching demonstration based on exact skill matching. It is **not an AI/LLM model yet**; the deterministic scoring is an auditable first step toward an AI recruitment workflow.

This is newly written portfolio code, not the code of Wajad or any employer.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open `http://localhost:8000/docs` for the interactive API. Run `pytest -q`.

## Example
```bash
curl -X POST http://localhost:8000/evaluate -H 'Content-Type: application/json' -d '{"job_title":"Backend Engineer","required_skills":["Python","FastAPI","Redis"],"candidate_name":"Demo Candidate","resume_text":"Backend engineer experienced with Python and FastAPI microservices"}'
```

## Roadmap
- PostgreSQL persistence and authenticated roles
- Document extraction and redaction
- Consent-aware LLM-assisted extraction with human review
- Fairness assessment, logging, retries, and evaluation datasets
