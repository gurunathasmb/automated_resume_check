import streamlit as st
import requests

BACKEND_URL = "http://localhost:5000/evaluate"

st.title("📄 Automated Resume Relevance Check System")

uploaded_resume = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf","docx"])
uploaded_jd = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if uploaded_resume and uploaded_jd:
    resume_path = f"temp_resume.{uploaded_resume.name.split('.')[-1]}"
    jd_path = "temp_jd.txt"
    
    with open(resume_path, "wb") as f:
        f.write(uploaded_resume.getbuffer())
    with open(jd_path, "wb") as f:
        f.write(uploaded_jd.getbuffer())

    response = requests.post(BACKEND_URL, json={"resume_path": resume_path, "job_path": jd_path})
    result = response.json()

    st.subheader("✅ Evaluation Result")
    st.write(f"**Relevance Score:** {result['relevanceScore']}")
    st.write(f"**Verdict:** {result['verdict']}")
    st.write(f"**Missing Skills:** {', '.join(result['missingSkills'])}")
    st.write(f"**Feedback:** {result['feedback']}")
