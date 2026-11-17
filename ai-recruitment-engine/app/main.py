from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re

app = FastAPI(title="Recruitment Matching API", version="0.1.0")

class MatchRequest(BaseModel):
    job_title: str = Field(min_length=2)
    required_skills: list[str] = Field(min_length=1)
    candidate_name: str = Field(min_length=1)
    resume_text: str = Field(min_length=10)

def skill_matches(skills: list[str], resume_text: str) -> dict:
    # Deterministic baseline: intentionally NOT an LLM or semantic ranking system.
    normalized = resume_text.casefold()
    matched = [skill for skill in skills if re.search(r"(?<!\w)" + re.escape(skill.casefold()) + r"(?!\w)", normalized)]
    return {"matched_skills": matched, "missing_skills": [s for s in skills if s not in matched], "score": round(100 * len(matched) / len(skills))}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/evaluate")
def evaluate(req: MatchRequest):
    result = skill_matches(req.required_skills, req.resume_text)
    return {"candidate_name": req.candidate_name, "job_title": req.job_title, **result, "method": "exact keyword baseline"}
