from PyPDF2 import PdfReader
import os

abs_path = os.path.abspath(r"test_scripts\sample_job.pdf")
reader = PdfReader(abs_path)
text = ""

for page in reader.pages:
    text += page.extract_text() or ""  # Use empty string if None

print("✅ Extracted text from PDF:\n")
print(text[:500])
