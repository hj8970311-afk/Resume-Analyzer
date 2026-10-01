"""
Extracts known skills from a block of text using keyword matching.
This is intentionally simple (no heavy NLP model needed) so it runs
fast and reliably without extra downloads.
"""
import re
from app.skills_database import SKILLS_DATABASE


def _normalize(text: str) -> str:
    return text.lower()


def extract_skills(text: str) -> list:
    """
    Returns a sorted list of skills (as they appear in SKILLS_DATABASE)
    found within the given text.
    """
    normalized_text = _normalize(text)
    found_skills = []

    for skill in SKILLS_DATABASE:
        skill_lower = skill.lower()
        # Build a regex that matches the skill as a whole phrase,
        # allowing for word boundaries. Escape special regex chars
        # like "c++" or "c#".
        pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill_lower) + r"(?![a-zA-Z0-9])"
        if re.search(pattern, normalized_text):
            found_skills.append(skill)

    return sorted(set(found_skills))
