# AI Resume Analyzer API

AI-powered API that analyzes resumes and matches them with job descriptions.

## Features

- Resume skill extraction
- Candidate evaluation
- Job description matching
- Missing skills detection
- Resume improvement suggestions

## Tech Stack

- Python
- FastAPI
- Pydantic
- Swagger API

## Endpoints

### Analyze Resume

POST /analyze

Example request:

{
 "resume_text": "...",
 "job_description": "..."
}

## Example Response

- match_score
- matched_skills
- missing_skills
- strengths
- weaknesses
- suggestions

## Run locally

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn app.main:app --reload