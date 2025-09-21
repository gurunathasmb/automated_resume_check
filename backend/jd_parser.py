from embeddings import semantic_similarity

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
    # Hard match
    hard_score = sum([1 for skill in jd_data["must_have_skills"] if skill.lower() in resume_text.lower()])
    hard_score = hard_score / len(jd_data["must_have_skills"]) * 50

    # Soft match
    jd_combined_text = " ".join(jd_data["must_have_skills"] + jd_data["good_to_have_skills"])
    soft_score = semantic_similarity(resume_text, jd_combined_text) * 40

    # Bonus
    bonus_score = 10 if "certification" in resume_text.lower() else 0

    total_score = hard_score + soft_score + bonus_score

    missing_skills = [skill for skill in jd_data["must_have_skills"] if skill.lower() not in resume_text.lower()]
    verdict = "High" if total_score >= 70 else "Medium" if total_score >= 50 else "Low"
    feedback = f"Add missing skills: {', '.join(missing_skills)}"

    return {
        "relevanceScore": round(total_score, 2),
        "missingSkills": missing_skills,
        "verdict": verdict,
        "feedback": feedback
    }
