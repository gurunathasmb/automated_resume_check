from flask import Flask, request, jsonify
from resume_parser import parse_resume
from jd_parser import parse_jd
from scoring import evaluate

app = Flask(__name__)

@app.route("/evaluate", methods=["POST"])
def evaluate_resume():
    data = request.json
    resume_path = data.get("resume_path")
    jd_path = data.get("job_path")

    # Parse files
    resume_text = parse_resume(resume_path)
    jd_data = parse_jd(jd_path)

    # Evaluate resume
    result = evaluate(resume_text, jd_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
