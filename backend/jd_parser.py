def parse_jd(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    # Simplified: extract skills (you can extend this with NLP)
    return {
        "title": "Data Scientist",
        "must_have_skills": ["Python", "ML", "SQL"],
        "good_to_have_skills": ["AWS", "Docker"],
        "qualifications": ["B.Tech", "M.Tech"]
    }
