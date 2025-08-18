import csv
import os

filename = "skills_database.csv"
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

"""
# ---------------- Example Usage ----------------
# Initialize dictionary only the first time
career_skills = {
    "Electrical Engineer": ["Circuit Design", "MATLAB", "Power Systems"],
    "Software Engineer": ["Python", "Java", "SQL"],
}

# Load existing data
skills_data = load_skills()

# Merge starter dictionary into CSV
for career, skills in career_skills.items():
    for skill in skills:
        add_new_skill(career, skill)

# Dynamically add one skill
add_new_skill("Software Engineer", "Git")

# Dynamically add multiple skills
add_multiple_skills("AI/ML Developer", ["TensorFlow", "PyTorch", "Machine Learning"])
"""