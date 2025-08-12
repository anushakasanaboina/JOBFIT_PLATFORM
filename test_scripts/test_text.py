import os

abs_path = os.path.abspath(r"test_scripts\sample_job.txt")
with open(abs_path, "r", encoding="utf-8") as f:
    text = f.read()

print("✅ Extracted text from TXT:\n")
print(text[:500])
