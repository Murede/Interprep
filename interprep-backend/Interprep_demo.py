from Interprep_MVP import InterPrepUser

def main():
    print("🚀 Welcome to Interprep MVP Demo 🚀")
    
    
    # Create a user 
    user = InterPrepUser()
    
    
    # Step 1: Collect user profile info 
    user.get_first_name()
    user.get_last_name()
    user.get_email()
    user.get_school()
    user.get_major()
    user.get_project_link()
    
    # Step 2: Download resume and extract skills 
    career_choice = input("\nEnter your career (e.g., 'Software Engineer', 'Electrical Engineer'): ").strip()
    user.extract_resume_skills(career=career_choice, file_path="skills_database.csv")
    
    # Step 3:  Debug Resume Processing 
    user.debug_resume_processing(career_choice, file_path="skills_database.csv")

   
    # Step 4: Match skills from CSV
    results = user.match_skills_from_csv(career=career_choice, file_path="skills_database.csv")
    print("\n🔎 Skill Matching Results:")
    print(f"Matched Skills: {results['matched']}")
    print(f"Missing Skills: {results['missing']}")
main()
