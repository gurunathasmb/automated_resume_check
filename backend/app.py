from flask import Flask, request, jsonify
from resume_parser import parse_resume_file
from scoring import evaluate, parse_jd_text

app = Flask(__name__)

@app.route("/evaluate-files", methods=["POST"])
def evaluate_files():
    try:
        # Get uploaded files
        resume_file = request.files.get('resume')
        jd_file = request.files.get('jd')

        if not resume_file or not jd_file:
            return jsonify({"error": "Resume or JD file missing"}), 400

        # Parse resume and JD
        resume_text = parse_resume_file(resume_file)
        jd_text = jd_file.read().decode("utf-8")
        jd_data = parse_jd_text(jd_text)

        # Evaluate
        result = evaluate(resume_text, jd_data)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
