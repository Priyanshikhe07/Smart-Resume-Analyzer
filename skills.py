SKILLS = [
    "python", "sql", "git", "machine learning",
    "data science", "algorithms", "data structures",
    "oop", "debugging", "aws", "docker"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills