import pdfplumber
import docx2txt

def parse_resume_file(file):
    """
    Parses a PDF or DOCX file from memory (Streamlit upload)
    """
    filename = file.filename.lower()
    text = ""

    if filename.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            text = "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif filename.endswith(".docx"):
        text = docx2txt.process(file)
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")
    return text
