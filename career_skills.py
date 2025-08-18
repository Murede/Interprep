import csv
import os

# ---------- Load existing data or initialize ----------
def load_skills():
    existing_data = {}
    if os.path.exists(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_data[row["Career"]] = row["Skills"].split(";")
    return existing_data

# ---------- Save updated skills back to CSV ----------
def save_skills(skills_dict):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Career", "Skills"])
        for career, skills in skills_dict.items():
            writer.writerow([career, ";".join(sorted(set(skills)))])

# ---------- Add a new skill ----------
def add_new_skill(career, skill):
    skills_dict = load_skills()

    if career not in skills_dict:
        skills_dict[career] = []

    if skill not in skills_dict[career]:
        skills_dict[career].append(skill)
        print(f"✅ Added {skill} to {career}")
    else:
        print(f"⚠️ {skill} already exists for {career}")

    save_skills(skills_dict)

# ---------- Add multiple skills (optional helper) ----------
def add_multiple_skills(career, skill_list):
    for skill in skill_list:
        add_new_skill(career, skill)
career_skills = {
    "Foundational": [
        "Mathematics",
        "Natural Sciences",
        "Humanities and Social Sciences"
    ],
    "Technical": [
        "Design",
        "Engineering Tools",
        "Risk, Uncertainty, and Failure",
        "Safety",
        "Systems Engineering",
        "Sustainability",
        "Manufacturing and Construction",
        "Operations and Maintenance",
        "Quality Control and Quality Assurance",
        "Technical Breadth",
        "Technical Depth"
    ],
    "Professional Practice": [
        "Communication",
        "Ethical Responsibility",
        "Global Knowledge and Awareness",
        "Business Aspects of Engineering",
        "Leadership",
        "Lifelong Learning",
        "Project Management",
        "Public Policy and Engineering",
        "Teamwork",
        "Historical Perspective",
        "Legal Aspects of Engineering",
        "Professional Attitudes"
    ],
    "Electrical Engineer": [
        "Circuit Design", "MATLAB", "Power Systems", "PCB Design", "Microcontrollers", "AutoCAD Electrical"
    ],
    "Software Engineer": [
        "Python", "Java", "C++", "Algorithms", "Data Structures", "Git", "Agile Development", "SQL"
    ],
    "AI/ML Developer": [
        "Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "NLP", "Data Analysis", "Model Deployment"
    ],
    "UX Designer": [
        "Wireframing", "User Research", "Figma", "Prototyping", "Usability Testing", "Information Architecture", "UI Design"
    ]
}

filename = "skills_database.csv"

# Step 1: Check if file exists and read current contents
existing_data = {}
if os.path.exists(filename):
    with open(filename, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_data[row["Career"]] = row["Skills"].split(";")

# Step 2: Merge new skills with existing ones (avoid duplicates)
for career, skills in career_skills.items():
    if career in existing_data:
        # Merge and deduplicate
        merged_skills = set(existing_data[career] + skills)
        existing_data[career] = list(merged_skills)
    else:
        existing_data[career] = skills

# Step 3: Write back to CSV (overwrite with updated data)
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Career", "Skills"])
    for career, skills in existing_data.items():
        writer.writerow([career, ";".join(skills)])
