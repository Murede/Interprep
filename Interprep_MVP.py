from os import read
import re  # PyMuPDF for PDF parsing
from google.colab import files
import PyPDF2

class InterprepUser:
    # Interprep User Constructor(contains all the information for a single interprep user)
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.major = ""
        self.project_link = ""
        self.resume_text = ""
        self.resume_skills = []
        self.user_skills = []
        self.missing_skills = []
        self.learning_resources = {}
        learning_resources = {}
        # Example " {"Figma": ["https://www.learnpython.org", "https://www.coursera.org/specializations/python"]}
        self.skill_progress={}# preload with your dictionary
        # Example: {"Python": 40, "Verilog": 10, "PLC Programming": 0}


        """
        Work on creating a larger skill list and learning resources list

        2️⃣ Make resume skill extraction more powerful
          * Right now it’s hardcoded to check a small list. You could:

          * Load keywords from an external CSV/JSON so it’s easier to update.

          * Use NLP libraries (like spaCy) to extract technical skills dynamically from text.

          * Match skills case-insensitively and account for synonyms (“ML” → “Machine Learning”).

        4️⃣ Enhance the learning plan
          * Instead of just printing steps:

          * Break it into weekly or daily goals.

          * Add estimated time commitments.

          *  Track completion for each skill’s plan step.
        """


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

    # Getting personal project links(things like Github, MyHuggingFaces)
    def get_project_link(self):
        url_pattern = re.compile(r'^(https?://)?([\w\-]+\.)+[a-z]{2,}(/[\w\-./?%&=]*)?$')
        while True:
            link = input("Enter your personal project link (e.g., GitHub): ").strip()
            if url_pattern.match(link):
                self.project_link = link
                break
            else:
                print("Invalid link format. Try again.")


    # Need to come back here to find a way to keep keywords as a seperate dataset referenced
    # Extracting skills from the user resume
    def extract_resume_skills(self, file_path="skills_database.csv" ):
      # Upload the resume
      print("Upload your resume in PDF format: \n")

      uploaded_resume = files.upload()
      resume_filename = list(uploaded_resume.keys())[0]

      with open(resume_filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
          self.resume_text += page.extract_text()

      skills_dict = {}
      with open(file_path, mode="r") as file:
          reader = csv.DictReader(file)
          for row in reader:
              skills_dict[row["Career"].strip()] = [
                  s.strip() for s in row["Skills"].split(";")
              ]

        # Get the required skills for the career
      keywords = skills_dict.get(career, [])

      self.user_skills = [skill for skill in keywords if skill.lower() in self.resume_text.lower()]
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

    # Recomending the resources for the corresponding missing skill
    # Ned to update the learning resource list to match more skills
    def recommend_resources(self):
        if not self.missing_skills:
            print("No missing skills found!")
            return
        for skill in self.missing_skills:
            resources = self.learning_resources.get(skill, [])
            print(f"Skill: {skill}")
            for resource in resources:
                print(f"  Resource: {resource}")

    # Generate personalized learning plan for the missing students
    def generate_plan(self):
        print("\n📅 Suggested Learning Plan:")
        for i, skill in enumerate(self.missing_skills, start=1):
            resources = self.learning_resources.get(skill, [])
            print(f"Step {i}: Learn {skill}")
            for r in resources:
                print(f"  - {r}")

    def update_skill_progress(self, skill, progress):
        if skill in self.skill_progress:
            self.skill_progress[skill] = max(0, min(100, progress)) # Clamp between 0-100
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
# Example usage:
# app = InterprepApp()
# app.get_first_name()
# app.upload_and_parse_resume()
# app.extract_skills_from_resume(["Python", "Prototyping", "Data Analysis"])
# app.match_skills(["Python", "Prototyping", "Machine Learning"])
# app.recommend_resources()
# app.generate_plan()
