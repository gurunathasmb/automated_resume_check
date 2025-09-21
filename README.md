# Automated Resume Relevance Check System

## Overview
This project is an **AI-powered resume evaluation system** that automates the process of matching resumes against job descriptions. It provides a **Relevance Score**, highlights **missing skills**, gives a **fit verdict**, and offers **personalized feedback** to help candidates improve their resumes.

Built using **Python, Flask, Streamlit**, and **embedding-based semantic analysis**.

## Features
- Upload **Resume (PDF/DOCX)** and **Job Description (TXT)**.
- Generate **Relevance Score (0–100)**.
- Detect **missing skills** from the resume.
- Provide **Verdict** (High / Medium / Low suitability).
- Generate **feedback** for candidate improvement.
- **Semantic analysis** using embeddings for contextual matching.

## Tech Stack
- **Backend:** Python, Flask, REST API
- **Frontend:** Streamlit Dashboard
- **Resume Parsing:** pdfplumber, docx2txt
- **NLP / Semantic Matching:** SentenceTransformers, scikit-learn
- **Scoring:** Hard match (keywords) + Soft match (embedding similarity)
- **Data Storage:** Optional MongoDB (for multi-resume management)

## Folder Structure
```
automated_resume_check/
│
├── backend/                     # Flask AI backend
│   ├── app.py                   # Flask main server
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── scoring.py
│   ├── embeddings.py
│   └── requirements.txt
│
├── frontend/                    # Streamlit dashboard
│   ├── app.py
│   └── utils.py
│
├── sample_data/                 # Sample resumes & JDs
└── README.md
```

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/automated_resume_check.git
cd automated_resume_check
```

2. **Install backend dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Start Flask backend**
```bash
python app.py
```

4. **Start Streamlit frontend**
```bash
cd ../frontend
streamlit run app.py
```

5. **Access dashboard**
Open browser at: `http://localhost:8501`

## Usage
1. Upload a **Resume (PDF/DOCX)**.
2. Upload a **Job Description (TXT)**.
3. Click **Evaluate**.
4. The system returns:
   - **Relevance Score**
   - **Verdict (High/Medium/Low)**
   - **Missing Skills**
   - **Feedback for improvement**

## Extending the System
- Add **MongoDB** for storing multiple resumes and evaluation history.
- Use **OpenAI GPT / HuggingFace** for richer feedback generation.
- Enhance **JD parsing** with NLP to extract skills automatically.
- Add **batch processing** for evaluating thousands of resumes at scale.

## Quick Start with Sample Files
- Place sample resumes (PDF/DOCX) in `sample_data/`.
- Place sample job descriptions (TXT) in `sample_data/`.
- Use the Streamlit dashboard to upload these files and see results immediately.

## License
This project is released under the **MIT License**.

