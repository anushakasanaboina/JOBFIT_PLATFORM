# JobFit Platform

**JobFit Platform** is a simple, rule-based job matching web application built with Flask. It lets users upload resumes and job descriptions (PDF, DOCX, TXT), extracts text, and compares technology keywords to calculate a match percentage. It highlights matched and missing skills to help users quickly evaluate their job fit.

## Features

- Upload resumes and job descriptions in multiple formats  
- Extract text from uploaded files using `PyPDF2` and `docx2txt`  
- Keyword-based skill matching with support for synonyms and variants  
- Displays match percentage and lists matched/missing skills  
- Clean, user-friendly interface built with Flask  

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anushakasanaboina/JOBFIT_PLATFORM.git
   cd JOBFIT_PLATFORM
2.Create and activate a Python virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3.Install dependencies:
  pip install -r requirements.txt
4.Run the Flask app:
  python app.py
5.Open your browser at http://127.0.0.1:5000

Project Structure

 JOBFIT_PLATFORM/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── css/
│   └── js/
├── upload/
└── README.md

Dependencies
Flask
PyPDF2
docx2txt
(You can add these to requirements.txt)

Documentation
 (Development diaries and detailed documentation are available to help understand the project progress and design decisions)
Day 1: Project setup and file upload
Day 2: Text extraction from PDF, DOCX, and TXT files
Day 3: Technology keyword matching and result display
 ...Feel free to refer to these docs for insights on the project’s evolution and implementation details...

License
MIT License



