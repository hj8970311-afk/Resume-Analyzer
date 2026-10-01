"""
AI Resume Analyzer & Interview Coach - FastAPI backend.

Run with:
    uvicorn app.main:app --reload

Then open http://127.0.0.1:8000 in your browser.
"""
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.resume_parser import extract_resume_text
from app.analyzer import analyze_resume_vs_jd
from app.interview_questions import generate_interview_questions
from app.roadmap import generate_learning_roadmap

app = FastAPI(title="AI Resume Analyzer & Interview Coach")

# Allow the frontend (served from the same app, but keep this open
# in case you split frontend/backend later during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...),
):
    if not job_description or not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    file_bytes = await resume_file.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded resume file is empty.")

    try:
        resume_text = extract_resume_text(resume_file.filename, file_bytes)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Could not extract any text from the resume. "
                   "If it's a scanned/image-based PDF, try a text-based one."
        )

    analysis = analyze_resume_vs_jd(resume_text, job_description)
    interview_questions = generate_interview_questions(analysis["resume_skills"])
    roadmap = generate_learning_roadmap(analysis["missing_skills"])

    return JSONResponse({
        "ats_score": analysis["ats_score"],
        "semantic_similarity": analysis["semantic_similarity"],
        "skill_match_percent": analysis["skill_match_percent"],
        "resume_skills": analysis["resume_skills"],
        "jd_skills": analysis["jd_skills"],
        "matched_skills": analysis["matched_skills"],
        "missing_skills": analysis["missing_skills"],
        "interview_questions": interview_questions,
        "learning_roadmap": roadmap,
    })


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Serve the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")
