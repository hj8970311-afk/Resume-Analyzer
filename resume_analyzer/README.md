# AI Resume Analyzer & Interview Coach

An end-to-end web app that:
- Extracts text from an uploaded resume (PDF/DOCX)
- Extracts skills using keyword-based NLP matching
- Compares the resume against a pasted job description
- Predicts an ATS-style match score
- Highlights matched vs. missing skills
- Generates relevant interview questions based on your skills
- Suggests a learning roadmap for missing skills

## Tech Stack
- **Backend:** Python, FastAPI
- **NLP:** Sentence-Transformers (semantic similarity) + keyword-based skill extraction
- **Parsing:** pdfplumber (PDF), python-docx (DOCX)
- **Frontend:** HTML, CSS, JavaScript (no framework needed)

## Project Structure
```
resume_analyzer/
├── app/
│   ├── main.py                 # FastAPI app & routes
│   ├── resume_parser.py        # PDF/DOCX text extraction
│   ├── skill_extractor.py      # Keyword-based skill extraction
│   ├── skills_database.py      # List of known skills
│   ├── analyzer.py             # ATS score + comparison logic
│   ├── interview_questions.py  # Question generation
│   └── roadmap.py              # Learning roadmap suggestions
├── static/
│   └── index.html              # Frontend (single file)
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Install Python
Make sure you have Python 3.9+ installed.

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
> Note: the first install will download the `sentence-transformers` model
> dependencies (~90MB). This requires an internet connection once.

### 4. Run the app
```bash
uvicorn app.main:app --reload
```

### 5. Open in browser
Go to: **http://127.0.0.1:8000**

Upload a resume (PDF or DOCX) and paste a job description, then click
"Analyze Resume".

## How It Works

1. **Resume Parsing** — `resume_parser.py` extracts raw text from the
   uploaded PDF/DOCX file.
2. **Skill Extraction** — `skill_extractor.py` scans the text against a
   curated list of ~150 technical & soft skills (`skills_database.py`)
   using word-boundary regex matching.
3. **Comparison** — `analyzer.py` does two things:
   - Computes **semantic similarity** between resume and JD using
     Sentence-Transformers embeddings (captures meaning, not just
     exact keyword overlap).
   - Computes **skill overlap** (what % of JD skills appear in the resume).
   - Combines both into a weighted **ATS score** (60% skill match,
     40% semantic similarity — since real ATS systems are mostly
     keyword-driven).
4. **Interview Questions** — `interview_questions.py` picks relevant
   questions from a curated question bank based on skills found in
   your resume, with a generic fallback for skills not in the bank.
5. **Learning Roadmap** — `roadmap.py` maps each missing skill to a
   free learning resource.

## Extending This Project (Advanced Ideas)
If you want to go beyond the basics for your major project submission,
consider adding:
- **Resume formatting checks** (font consistency, section headers, length)
- **User accounts + history** (store past analyses in a database, e.g. SQLite)
- **LLM-powered feedback** (use an LLM API to generate personalized,
  natural-language feedback instead of static templates)
- **Resume rewriting suggestions** (bullet point improvements)
- **Score trend chart** if a user uploads multiple resume versions
- **Deploy it** on Render, Railway, or Hugging Face Spaces so you can
  share a live link in your project report

## Troubleshooting
- **"Could not extract any text from the resume"** — your PDF is likely
  a scanned image rather than text-based. Try a resume exported directly
  from Word/Google Docs as PDF.
- **Slow first request** — the sentence-transformers model loads into
  memory on first use; subsequent requests are much faster.
- **Port already in use** — run with a different port:
  `uvicorn app.main:app --reload --port 8001`
