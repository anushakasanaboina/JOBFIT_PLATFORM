import docx2txt
import os

abs_path = os.path.abspath(r"test_scripts\sample_resume.docx")
text = docx2txt.process(abs_path)
print("✅ Extracted text from DOCX:\n")
print(text[:500])
