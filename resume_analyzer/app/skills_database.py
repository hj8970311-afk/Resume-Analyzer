"""
A curated list of common technical and soft skills used for
keyword-based extraction from resumes and job descriptions.

Feel free to add more skills to this list to improve accuracy.
"""

SKILLS_DATABASE = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "c",
    "go", "golang", "rust", "ruby", "php", "swift", "kotlin", "scala",
    "r", "matlab", "perl", "dart",

    # Web Development
    "html", "css", "react", "reactjs", "angular", "vue", "vuejs",
    "next.js", "nextjs", "node.js", "nodejs", "express", "express.js",
    "django", "flask", "fastapi", "spring", "spring boot", "asp.net",
    "bootstrap", "tailwind", "tailwind css", "jquery", "webpack",
    "graphql", "rest api", "restful api", "api development",

    # Data / ML / AI
    "machine learning", "deep learning", "artificial intelligence",
    "nlp", "natural language processing", "computer vision",
    "data science", "data analysis", "data engineering",
    "data visualization", "statistics", "pandas", "numpy",
    "scikit-learn", "sklearn", "tensorflow", "keras", "pytorch",
    "sentence transformers", "transformers", "huggingface",
    "opencv", "spacy", "nltk", "llm", "large language models",
    "generative ai", "prompt engineering", "langchain",

    # Databases
    "sql", "mysql", "postgresql", "postgres", "mongodb", "sqlite",
    "redis", "oracle", "database design", "nosql", "firebase",
    "elasticsearch", "dynamodb", "supabase",

    # Cloud / DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes",
    "ci/cd", "jenkins", "git", "github", "gitlab", "linux",
    "terraform", "ansible", "devops", "microservices",
    "serverless", "cloud computing", "nginx",

    # Tools
    "excel", "power bi", "tableau", "jira", "figma", "postman",
    "vs code", "jupyter", "google colab",

    # Testing
    "unit testing", "pytest", "selenium", "test automation",
    "software testing", "qa",

    # Soft Skills
    "communication", "teamwork", "leadership", "problem solving",
    "critical thinking", "time management", "adaptability",
    "collaboration", "project management", "agile", "scrum",
    "presentation skills", "analytical skills", "creativity",

    # Mobile
    "android", "ios", "react native", "flutter",

    # Misc CS fundamentals
    "data structures", "algorithms", "oop",
    "object oriented programming", "system design",
    "operating systems", "computer networks",
]

# Normalize to lowercase set for fast lookups, keep original list for display
SKILLS_SET = set(s.lower() for s in SKILLS_DATABASE)
