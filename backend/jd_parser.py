def parse_jd(file_path):
    # Simple text extraction for JD
    with open(file_path, "r") as f:
        text = f.read()
    
    # Extract required fields (simplified)
    jd_data = {
        "title": "Data Scientist",
        "must_have_skills": ["Python", "ML", "SQL"],
        "good_to_have_skills": ["AWS", "Docker"],
        "qualifications": ["B.Tech", "M.Tech"]
    }
    return jd_data
