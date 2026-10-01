"""
Core analysis logic:
- Compares resume text against a job description
- Computes an ATS-style match score
- Identifies missing skills
"""
from sentence_transformers import SentenceTransformer, util
from app.skill_extractor import extract_skills

# Load the model once at import time (keeps requests fast).
# This is a small, fast model well suited for semantic similarity.
_model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_semantic_similarity(resume_text: str, jd_text: str) -> float:
    """
    Returns a similarity score between 0 and 100 based on sentence
    embeddings of the two texts.
    """
    embeddings = _model.encode([resume_text, jd_text], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
    # cos_sim ranges roughly -1 to 1; clamp and scale to 0-100
    similarity = max(0.0, min(1.0, similarity))
    return round(similarity * 100, 2)


def compute_skill_match(resume_skills: list, jd_skills: list) -> dict:
    resume_set = set(s.lower() for s in resume_skills)
    jd_set = set(s.lower() for s in jd_skills)

    if not jd_set:
        matched_pct = 0.0
        matched = []
        missing = []
    else:
        matched = sorted(jd_set & resume_set)
        missing = sorted(jd_set - resume_set)
        matched_pct = round((len(matched) / len(jd_set)) * 100, 2)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "skill_match_percent": matched_pct,
    }


def compute_ats_score(semantic_score: float, skill_match_percent: float) -> float:
    """
    Weighted combination of semantic similarity and keyword/skill overlap.
    Skill overlap is weighted higher since most real ATS systems are
    primarily keyword-driven.
    """
    ats_score = (0.4 * semantic_score) + (0.6 * skill_match_percent)
    return round(ats_score, 2)


def analyze_resume_vs_jd(resume_text: str, jd_text: str) -> dict:
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    semantic_score = compute_semantic_similarity(resume_text, jd_text)
    skill_result = compute_skill_match(resume_skills, jd_skills)
    ats_score = compute_ats_score(semantic_score, skill_result["skill_match_percent"])

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": skill_result["matched_skills"],
        "missing_skills": skill_result["missing_skills"],
        "skill_match_percent": skill_result["skill_match_percent"],
        "semantic_similarity": semantic_score,
        "ats_score": ats_score,
    }
