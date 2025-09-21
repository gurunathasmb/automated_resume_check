from embeddings import semantic_similarity
from fuzzywuzzy import fuzz
def parse_jd_text(jd_text):
    """
    Convert raw JD text into structured fields.
    You can enhance this with NLP to auto-extract skills.
    """
    return {
        "title": "Data Scientist",
        "must_have_skills": ["Python", "ML", "SQL"],
        "good_to_have_skills": ["AWS", "Docker"],
        "qualifications": ["B.Tech", "M.Tech"]
    }

def evaluate(resume_text, jd_data):
    resume_text_lower = resume_text.lower()
    hard_score = 0
    missing_skills = []

    for skill in jd_data["must_have_skills"]:
        skill_lower = skill.lower()

        # 1. Exact substring match
        if skill_lower in resume_text_lower:
            hard_score += 1
            continue

        # 2. Fuzzy match
        ratio = fuzz.partial_ratio(skill_lower, resume_text_lower)
        if ratio >= 80:
            hard_score += 1
            continue

        # 3. Semantic similarity
        similarity = semantic_similarity(skill, resume_text)
        if similarity >= 0.65:
            hard_score += 1
        else:
            missing_skills.append(skill)

    hard_score = hard_score / len(jd_data["must_have_skills"]) * 50

    # Soft match: overall semantic fit
    jd_combined_text = " ".join(jd_data["must_have_skills"] + jd_data["good_to_have_skills"])
    soft_score = float(semantic_similarity(resume_text, jd_combined_text) * 40)

    # Bonus
    bonus_score = 10 if "certification" in resume_text_lower else 0

    total_score = float(hard_score + soft_score + bonus_score)

    verdict = "High" if total_score >= 70 else "Medium" if total_score >= 50 else "Low"
    feedback = "Add missing skills: " + ", ".join(missing_skills) if missing_skills else "All must-have skills present!"

    return {
        "relevanceScore": round(total_score, 2),
        "missingSkills": missing_skills,
        "verdict": verdict,
        "feedback": feedback
    }