def evaluate(resume_text, jd_data):
    # Hard match (keywords)
    hard_score = sum([1 for skill in jd_data["must_have_skills"] if skill.lower() in resume_text.lower()])
    hard_score = hard_score / len(jd_data["must_have_skills"]) * 50

    # Soft match (dummy semantic score)
    soft_score = 35  # Replace with embeddings + cosine similarity if needed

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
