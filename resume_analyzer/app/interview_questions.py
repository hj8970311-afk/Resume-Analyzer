"""
Generates interview questions based on the skills detected in a resume.
Uses a template bank keyed by skill/category, with a generic fallback
so every detected skill produces at least one relevant question.
"""

QUESTION_BANK = {
    "python": [
        "What are Python's key data structures and when would you use each?",
        "Explain the difference between a list and a tuple in Python.",
        "How does Python's garbage collection work?",
    ],
    "java": [
        "Explain the difference between JVM, JRE, and JDK.",
        "What is the difference between an interface and an abstract class in Java?",
    ],
    "sql": [
        "What is the difference between INNER JOIN and LEFT JOIN?",
        "How would you optimize a slow-running SQL query?",
    ],
    "machine learning": [
        "How do you handle overfitting in a machine learning model?",
        "Explain the bias-variance tradeoff.",
        "Walk me through how you would evaluate a classification model.",
    ],
    "deep learning": [
        "Explain how backpropagation works.",
        "What is the vanishing gradient problem and how do you address it?",
    ],
    "nlp": [
        "How would you build a text classification pipeline from scratch?",
        "What is the difference between stemming and lemmatization?",
    ],
    "natural language processing": [
        "Explain how word embeddings capture semantic meaning.",
    ],
    "react": [
        "Explain the difference between state and props in React.",
        "What are React hooks and why were they introduced?",
    ],
    "django": [
        "Explain Django's MVT architecture.",
        "How does Django handle database migrations?",
    ],
    "fastapi": [
        "How does FastAPI achieve high performance compared to Flask?",
        "How would you handle request validation in FastAPI?",
    ],
    "docker": [
        "What is the difference between a Docker image and a container?",
        "How would you reduce the size of a Docker image?",
    ],
    "aws": [
        "What AWS services would you use to deploy a scalable web app?",
    ],
    "data structures": [
        "Explain the difference between a stack and a queue.",
        "When would you use a hash map over an array?",
    ],
    "algorithms": [
        "Explain the time complexity of quicksort in the best and worst case.",
    ],
    "system design": [
        "How would you design a URL shortening service?",
    ],
    "communication": [
        "Tell me about a time you had to explain a technical concept to a non-technical stakeholder.",
    ],
    "leadership": [
        "Describe a situation where you had to lead a team through a difficult project.",
    ],
    "project management": [
        "How do you prioritize tasks when managing multiple deadlines?",
    ],
    "agile": [
        "Explain the role of a sprint retrospective in Agile development.",
    ],
}

GENERIC_FALLBACK_QUESTIONS = [
    "Can you describe a project where you applied {skill}?",
    "What challenges have you faced while working with {skill}, and how did you solve them?",
]


def generate_interview_questions(skills: list, max_questions: int = 12) -> list:
    """
    Returns a list of dicts: {"skill": ..., "question": ...}
    Prioritizes skills that have curated questions, then fills in
    generic questions for the remaining skills until max_questions is hit.
    """
    questions = []

    # First pass: curated questions
    for skill in skills:
        skill_key = skill.lower()
        if skill_key in QUESTION_BANK:
            for q in QUESTION_BANK[skill_key]:
                questions.append({"skill": skill, "question": q})
                if len(questions) >= max_questions:
                    return questions

    # Second pass: generic fallback for skills without curated questions
    for skill in skills:
        skill_key = skill.lower()
        if skill_key not in QUESTION_BANK:
            template = GENERIC_FALLBACK_QUESTIONS[0]
            questions.append({
                "skill": skill,
                "question": template.format(skill=skill)
            })
            if len(questions) >= max_questions:
                return questions

    return questions
