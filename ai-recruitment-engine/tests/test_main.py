from fastapi.testclient import TestClient
from app.main import app, skill_matches
client = TestClient(app)

def test_skills_are_case_insensitive():
    result = skill_matches(["Python", "Java"], "Experienced with PYTHON and Docker")
    assert result["matched_skills"] == ["Python"]
    assert result["score"] == 50

def test_api():
    response = client.post("/evaluate", json={"job_title":"Backend Engineer","required_skills":["FastAPI"],"candidate_name":"Demo","resume_text":"Built APIs using FastAPI in Python"})
    assert response.status_code == 200
    assert response.json()["score"] == 100
