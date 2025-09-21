import pdfplumber
import docx2txt

def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages])
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    else:
        text = ""
    return text
