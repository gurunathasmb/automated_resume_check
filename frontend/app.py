import streamlit as st
import requests

st.title("📄 Automated Resume Relevance Check System")

uploaded_resume = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf","docx"])
uploaded_jd = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if uploaded_resume and uploaded_jd:
    try:
        files = {
            "resume": (uploaded_resume.name, uploaded_resume.getvalue()),
            "jd": (uploaded_jd.name, uploaded_jd.getvalue())
        }

        response = requests.post("http://localhost:5000/evaluate-files", files=files, timeout=10)
        result = response.json()

        if "error" in result:
            st.error(f"Backend error: {result['error']}")
        else:
            st.subheader("✅ Evaluation Result")
            st.write(f"**Relevance Score:** {result['relevanceScore']}")
            st.write(f"**Verdict:** {result['verdict']}")
            st.write(f"**Missing Skills:** {', '.join(result['missingSkills'])}")
            st.write(f"**Feedback:** {result['feedback']}")

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
