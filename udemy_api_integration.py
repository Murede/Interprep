import requests
import csv
import os
"""
# Use your Udemy API credentials
client_id = "TI8yW2XqSf7q70vzbxVzkS8j8GvSgujOwH3WOdAs"
client_secret = "bZjE9xaAf09PxXRKzbL0dMPK03hx05nS2EpIeCx7znvKh2Svz0M9dyf7kDppiuFds6AonvvKtdClYI2Kpf7UMR4lVfDmSqYRUiYyAP1pFmu758u522ULzMAZGimvh3qF"

resources_file = "learning_resources_database.csv"


# ----------------- AUTH -----------------
def get_access_token():
    url = "https://www.udemy.com/api-2.0/authorizations/"
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, auth=(client_id, client_secret), data=data)
    response.raise_for_status()
    return response.json()["access_token"]

# ----------------- FETCH COURSES -----------------
def fetch_udemy_courses(skill, token, page_size=5):
    url = f"https://www.udemy.com/api-2.0/courses/?search={skill}&page_size={page_size}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    return [
        {
            "skill": skill,
            "name": course["title"],
            "type": "Course",
            "link": f"https://www.udemy.com{course['url']}",
            "free": "No" if course.get("price") else "Yes"
        }
        for course in data.get("results", [])
    ]

# ----------------- SAVE TO CSV -----------------
def add_courses_to_csv(courses, filename=resources_file):
    file_exists = os.path.exists(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Skill", "Resource Name", "Type", "Link", "Free"])
        for course in courses:
            writer.writerow([course["skill"], course["name"], course["type"], course["link"], course["free"]])

# ----------------- MAIN -----------------
if __name__ == "__main__":
    try:
        token = get_access_token()
        print("✅ Successfully authenticated with Udemy API")

        skills_to_fetch = ["Python", "Machine Learning", "Circuit Design", "UX Design"]
        for skill in skills_to_fetch:
            print(f"\n📚 Fetching Udemy courses for: {skill}")
            courses = fetch_udemy_courses(skill, token)
            add_courses_to_csv(courses)
            print(f"   → Added {len(courses)} courses for {skill}")

    except requests.exceptions.HTTPError as e:
        print("❌ API Error:", e)

"""

import requests
import base64

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

def fetch_udemy_courses(skill, page_size=5):
    url = f"https://www.udemy.com/api-2.0/courses/?search={skill}&page_size={page_size}"
    credentials = f"{client_id}:{client_secret}"
    token = base64.b64encode(credentials.encode()).decode()

    headers = {"Authorization": f"Basic {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Example
print(fetch_udemy_courses("Python"))
