import re
import PyPDF2
import csv
import json


class InterPrepUser:
    # Interprep User Constructor (contains all the information for a single Interprep user)
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.school = ""
        self.major = ""
        self.project_link = ""
        self.resume_text = ""
        self.resume_skills = []
        self.user_skills = []
        self.missing_skills = []
        self.learning_resources = {}
        # Example: {"Figma": ["https://learnfigma.com", "https://coursera.org/figma"]}
        self.skill_progress = {}
        # Example: {"Python": 40, "Verilog": 10, "PLC Programming": 0}

    # Getting the user's first name
    def get_first_name(self):
        self.first_name = input("Enter your first name: ").strip()

    # Getting the user's last name
    def get_last_name(self):
        self.last_name = input("Enter your last name: ").strip()

    # Getting the user's email
    def get_email(self):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        while True:
            email_input = input("Enter your email address: ").strip()
            if re.match(email_pattern, email_input):
                self.email = email_input
                break
            else:
                print("Invalid email format. Try again.")

    # Getting the user's educational institution
    def get_school(self):
        self.school = input("Enter your educational institution: ").strip()

    # Getting the user's major
    def get_major(self):
        self.major = input("Enter your major: ").strip()

    # Getting personal project links (GitHub, HuggingFace, etc.)
    def get_project_link(self):
        url_pattern = re.compile(r'^(https?://)?([\w\-]+\.)+[a-z]{2,}(/[\w\-./?%&=]*)?$')
        while True:
            link = input("Enter your personal project link (e.g., GitHub): ").strip()
            if url_pattern.match(link):
                self.project_link = link
                break
            else:
                print("Invalid link format. Try again.")

    # Extracting skills from the user resume
    def extract_resume_skills(self, career, file_path="skills_database.csv"):
        # Ask user to enter their resume PDF path
        pdf_path = input("Please enter the path to your resume PDF (e.g., resumes/my_resume.pdf): ").strip()
        self.resume_text = ""  # reset text each time

        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    self.resume_text += page.extract_text()
        except FileNotFoundError:
            print("❌ Could not find the file. Please check the path and try again.")
            return []

        # Load skills from CSV
        skills_dict = {}
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                skills_dict[row["Career"].strip()] = [
                    s.strip() for s in row["Skills"].split(";")
                ]

        # Get the required skills for the selected career
        keywords = skills_dict.get(career, [])

        # Match skills from resume text
        self.user_skills = [
            skill for skill in keywords if skill.lower() in self.resume_text.lower()
        ]

        print(f"✅ Extracted skills from resume: {self.user_skills}")
        return self.user_skills

    def match_skills_from_csv(self, career, file_path="skills_database.csv"):
        """
        Loads skills from a CSV and matches them against the user's skills.
        """
        # Load skills from CSV
        skills_dict = {}
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                skills_dict[row["Career"].strip()] = [
                    s.strip() for s in row["Skills"].split(";")
                ]

        # Get the required skills for the career
        required_skills = skills_dict.get(career, [])

        # Compare
        matched = set(self.user_skills) & set(required_skills)
        self.missing_skills = set(required_skills) - set(self.user_skills)

        return {
            "matched": list(matched),
            "missing": list(self.missing_skills)
        }

    # Recommend resources for missing skills
    def recommend_resources(self):
        if not self.missing_skills:
            print("🎉 No missing skills found!")
            return
        for skill in self.missing_skills:
            resources = self.learning_resources.get(skill, [])
            print(f"Skill: {skill}")
            for resource in resources:
                print(f"  Resource: {resource}")

    # Generate personalized learning plan
    def generate_plan(self):
        print("\n📅 Suggested Learning Plan:")
        for i, skill in enumerate(self.missing_skills, start=1):
            resources = self.learning_resources.get(skill, [])
            print(f"Step {i}: Learn {skill}")
            for r in resources:
                print(f"  - {r}")

    def update_skill_progress(self, skill, progress):
        if skill in self.skill_progress:
            self.skill_progress[skill] = max(0, min(100, progress))  # Clamp 0–100
        else:
            print(f"{skill} is not in the current skill list.")

    def view_skill_progress(self):
        for skill, progress in self.skill_progress.items():
            print(f"{skill}: {progress}% complete")

    def save_profile(self, filename="profile.json"):
        with open(filename, "w") as f:
            json.dump(self.__dict__, f)

    def load_profile(self, filename="profile.json"):
        with open(filename, "r") as f:
            data = json.load(f)
            self.__dict__.update(data)

    def debug_resume_processing(self, career, file_path="skills_database.csv"):
        """
        Debugging helper to troubleshoot why skills aren't being extracted.
        """

        print("\n🔎 DEBUGGING RESUME PROCESSING 🔎")

        # 1. Preview extracted text
        print("\n----- Resume Text Preview -----")
        print(self.resume_text[:500] if self.resume_text else "⚠️ No text extracted from resume.")
        print("----- End Preview -----")

        # 2. Check available career keys in CSV
        skills_dict = {}
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                skills_dict[row["Career"].strip()] = [
                    s.strip() for s in row["Skills"].split(";")
                ]

        print("\n📂 Careers available in CSV:")
        print(list(skills_dict.keys())[:10], "...")  # show first 10 careers    

        # 3. Check if career exists
        if career.strip() not in skills_dict:
            print(f"⚠️ Career '{career}' not found in CSV. Did you mean one of these?")
            close_matches = [c for c in skills_dict.keys() if career.lower() in c.lower()]
            print("Possible matches:", close_matches if close_matches else "None")
        else:
            print(f"✅ Career '{career}' found in CSV.")

         # 4. Show the expected skills
        keywords = skills_dict.get(career.strip(), [])
        print(f"\n🎯 Skills expected for {career}: {keywords}")

        # 5. Test matching logic
        matched = [skill for skill in keywords if skill.lower() in self.resume_text.lower()]
        print(f"\n📝 Matched skills in resume: {matched if matched else 'None'}")
        print("🔎 DEBUGGING COMPLETE\n")
