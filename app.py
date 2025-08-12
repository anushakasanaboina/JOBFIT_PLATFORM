from flask import Flask, render_template, request
import os
import re
import docx2txt
from PyPDF2 import PdfReader

app = Flask(__name__)

# ✅ Folder to save uploaded files
UPLOAD_FOLDER = "upload"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Technology keywords with variants
TECH_KEYWORDS = {
    'python': ['python'],
    'java': ['java'],
    'c++': ['c++', 'cpp'],
    'flask': ['flask'],
    'django': ['django'],
    'react': ['react', 'reactjs'],
    'nodejs': ['nodejs', 'node.js', 'node'],
    'sql': ['sql', 'mysql', 'postgresql'],
    'mongodb': ['mongodb', 'mongo'],
    'apis': ['api', 'apis', 'rest api', 'restful'],
    'machine learning': ['machine learning', 'ml'],
    'deep learning': ['deep learning', 'dl'],
    'html': ['html'],
    'css': ['css'],
    'javascript': ['javascript', 'js'],
    'aws': ['aws', 'amazon web services'],
    'docker': ['docker']
}

# ✅ Extraction functions
def extract_text_from_docx(path):
    return docx2txt.process(path)

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".docx":
        return extract_text_from_docx(path)
    elif ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".txt":
        return extract_text_from_txt(path)
    else:
        return ""

# ✅ Improved Matching Logic
def match_technologies(resume_text, job_text):
    resume_text = resume_text.lower()
    job_text = job_text.lower()

    resume_tech = set()
    job_tech = set()

    for tech, variants in TECH_KEYWORDS.items():
        for variant in variants:
            pattern = r'\b' + re.escape(variant) + r'\b'
            if re.search(pattern, resume_text):
                resume_tech.add(tech)
            if re.search(pattern, job_text):
                job_tech.add(tech)

    matched_tech = resume_tech & job_tech
    missing_tech = job_tech - resume_tech

    match_percent = (len(matched_tech) / len(job_tech) * 100) if job_tech else 0
    return round(match_percent, 2), matched_tech, missing_tech

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        resume = request.files.get("resume")
        job = request.files.get("job")

        resume_text = ""
        job_text = ""
        match_percent = 0
        matched_tech = set()
        missing_tech = set()

        if resume:
            resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
            resume.save(resume_path)
            resume_text = extract_text(resume_path)
            print(f"Resume saved: {resume_path}")

        if job:
            job_path = os.path.join(UPLOAD_FOLDER, job.filename)
            job.save(job_path)
            job_text = extract_text(job_path)
            print(f"Job Description saved: {job_path}")

        if resume_text and job_text:
            match_percent, matched_tech, missing_tech = match_technologies(resume_text, job_text)
            print(f"✅ Match: {match_percent}% | Missing: {missing_tech}")

        return render_template(
            "result.html",
            match_percent=match_percent,
            matched_tech=matched_tech,
            missing_tech=missing_tech
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
