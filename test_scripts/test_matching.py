from nltk.corpus import stopwords

# Sample texts (replace these with your actual extracted texts)
resume_text = """
Python developer with experience in Flask and SQL databases.
Worked on backend APIs and data analysis.
"""

job_text = """
We need a Python Developer with knowledge of Flask, APIs, and SQL.
The candidate should have strong problem-solving skills.
"""

# 1. Lowercase
resume_text = resume_text.lower()
job_text = job_text.lower()

# 2. Split words
resume_words = resume_text.split()
job_words = job_text.split()

# 3. Remove stopwords
stop_words = set(stopwords.words("english"))
resume_keywords = [w for w in resume_words if w not in stop_words]
job_keywords = [w for w in job_words if w not in stop_words]

# 4. Find matches and missing
matched_keywords = set(resume_keywords) & set(job_keywords)
missing_keywords = set(job_keywords) - set(resume_keywords)

# 5. Calculate match percentage
match_percentage = (len(matched_keywords) / len(set(job_keywords))) * 100
match_percentage = round(match_percentage, 2)

# 6. Print results
print(f"✅ Match Percentage: {match_percentage}%")
print(f"🔑 Missing Keywords: {missing_keywords}")
