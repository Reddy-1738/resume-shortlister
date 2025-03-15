import os
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import fitz
import docx

model = SentenceTransformer("BAAI/bge-large-en-v1.5")


folder_path = "C:/Users/reddy/OneDrive/Desktop/projects/Resumes"
resume_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".pdf", ".docx"))]

if not resume_files:
    print(" Error: No valid resume files found.")
    exit()

job_descriptions = {
    "Python Developer": "Looking for a Python developer with experience in Flask and SQL.",
    "Java Developer": "Seeking a Java developer with expertise in Spring Boot and microservices.",
    "Frontend Developer": "Hiring a frontend developer skilled in React and JavaScript.",
    "Data Scientist": "Looking for a data scientist proficient in machine learning and Python.",
    "AI Engineer": "Hiring an AI engineer with experience in deep learning and NLP."
}

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text") + "\n"
    return text.strip()

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    return None

print("\nAvailable Job Roles:")
job_roles = list(job_descriptions.keys())
for idx, role in enumerate(job_roles, 1):
    print(f"{idx}. {role}")

selected_role = None
while selected_role is None:
    try:
        selected_index = int(input("\nEnter the number corresponding to the role you are applying for: ")) - 1
        if 0 <= selected_index < len(job_roles):
            selected_role = job_roles[selected_index]
        else:
            print(" Invalid selection. Please enter a valid number.")
    except ValueError:
        print(" Please enter a valid number.")

job_description = job_descriptions[selected_role]
job_embedding = model.encode(job_description)

results = []

for resume_file in resume_files:
    extracted_text = extract_text(resume_file)
    if not extracted_text:
        print(f" Error: Could not extract text from '{resume_file}'. Skipping...")
        continue

    resume_embedding = model.encode(extracted_text)
    match_percentage = util.cos_sim(resume_embedding, job_embedding).item() * 100

    results.append([os.path.basename(resume_file), selected_role, match_percentage])

results.sort(key=lambda x: x[2], reverse=True)

df = pd.DataFrame(results, columns=["Resume", "Selected Role", "Match Percentage"])

output_file = "resume_match.xlsx"
df.to_excel(output_file, index=False)
