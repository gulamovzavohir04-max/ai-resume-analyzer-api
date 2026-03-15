from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Resume Analyzer")

class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze_resume(data: ResumeRequest):

    resume_text = data.resume_text.lower()
    job_text = data.job_description.lower()

    skills_db = [
        "python",
        "sql",
        "fastapi",
        "django",
        "machine learning",
        "pandas",
        "scikit-learn",
        "docker",
        "git",
        "api",
        "javascript",
        "react",
        "aws",
        "linux"
    ]

    resume_skills = [skill for skill in skills_db if skill in resume_text]
    job_skills = [skill for skill in skills_db if skill in job_text]

    matched_skills = [skill for skill in resume_skills if skill in job_skills]
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]

    if len(job_skills) > 0:
        match_score = int((len(matched_skills) / len(job_skills)) * 100)
    else:
        match_score = 0

    strengths = []
    weaknesses = []
    suggestions = []

    if matched_skills:
        strengths.append("Resume matches some job requirements.")
    else:
        weaknesses.append("Resume does not match job requirements well.")

    if missing_skills:
        weaknesses.append("Some important job skills are missing in resume.")
        suggestions.append("Add missing skills if you really have them: " + ", ".join(missing_skills))

    if "experience" in resume_text:
        strengths.append("Work experience mentioned in resume.")
    else:
        weaknesses.append("Work experience missing.")
        suggestions.append("Add a clear experience section.")

    if "project" in resume_text or "projects" in resume_text:
        strengths.append("Projects section detected.")
    else:
        weaknesses.append("Projects not mentioned.")
        suggestions.append("Add project experience.")

    if "education" in resume_text:
        strengths.append("Education section present.")
    else:
        weaknesses.append("Education section missing.")
        suggestions.append("Add education section.")

    if match_score < 30:
        fit_level = "Low Match"
    elif match_score < 60:
        fit_level = "Medium Match"
    else:
        fit_level = "High Match"

    return {
        "match_score": match_score,
        "fit_level": fit_level,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }