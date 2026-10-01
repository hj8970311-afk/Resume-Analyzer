"""
Suggests learning resources for skills the candidate is missing,
relative to a target job description.
"""

RESOURCE_MAP = {
    "python": "Official Python docs + 'Automate the Boring Stuff with Python' (free online book)",
    "sql": "Mode Analytics SQL Tutorial (free) + LeetCode SQL practice problems",
    "machine learning": "Andrew Ng's Machine Learning Specialization (Coursera)",
    "deep learning": "DeepLearning.AI's Deep Learning Specialization (Coursera)",
    "nlp": "Hugging Face NLP Course (free, huggingface.co/learn)",
    "natural language processing": "Hugging Face NLP Course (free, huggingface.co/learn)",
    "docker": "Docker's official 'Get Started' guide + Docker Curriculum (free)",
    "kubernetes": "Kubernetes official docs 'Learn Kubernetes Basics'",
    "aws": "AWS Cloud Practitioner Essentials (free on AWS Skill Builder)",
    "react": "Official React docs (react.dev) 'Learn React' section",
    "django": "Django official tutorial ('Writing your first Django app')",
    "fastapi": "FastAPI official documentation tutorial (fastapi.tiangolo.com)",
    "data structures": "'Data Structures and Algorithms' course on freeCodeCamp (YouTube)",
    "algorithms": "NeetCode.io structured DSA roadmap + LeetCode practice",
    "system design": "'Grokking the System Design Interview' + ByteByteGo YouTube channel",
    "git": "Git official docs + 'Learn Git Branching' interactive tutorial",
    "agile": "Atlassian's free Agile Coach guide",
    "communication": "Toastmasters resources + Coursera 'Improving Communication Skills'",
    "leadership": "Coursera 'Leading People and Teams' specialization",
}

GENERIC_RESOURCE = "Search for a free course on {skill} via YouTube, Coursera, or freeCodeCamp"


def generate_learning_roadmap(missing_skills: list) -> list:
    """
    Returns a list of dicts: {"skill": ..., "resource": ...}
    """
    roadmap = []
    for skill in missing_skills:
        skill_key = skill.lower()
        resource = RESOURCE_MAP.get(skill_key, GENERIC_RESOURCE.format(skill=skill))
        roadmap.append({"skill": skill, "resource": resource})
    return roadmap
