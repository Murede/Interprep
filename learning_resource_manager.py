import csv
import os

resources_file = "learning_resources_database.csv"

def load_resources():
    resources = {}
    if os.path.exists(resources_file):
        with open(resources_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                skill = row["Skill"]
                if skill not in resources:
                    resources[skill] = []
                resources[skill].append({
                    "name": row["Resource Name"],
                    "type": row["Type"],
                    "link": row["Link"],
                    "free": row["Free"].lower() == "yes"
                })
    return resources

def add_resource(skill, name, type_, link, free="Yes"):
    file_exists = os.path.exists(resources_file)
    with open(resources_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Skill", "Resource Name", "Type", "Link", "Free"])
        writer.writerow([skill, name, type_, link, free])

def view_resources(skill):
    resources = load_resources()
    if skill in resources:
        print(f"\nResources for {skill}:")
        for r in resources[skill]:
            free_label = "Free" if r["free"] else "Paid"
            print(f"- {r['name']} ({r['type']}, {free_label}) → {r['link']}")
    else:
        print(f"No resources found for {skill}")

"""
# Add some resources
add_resource("Python", "Python for Everybody", "Course", "https://www.coursera.org/specializations/python", "Yes")
add_resource("Python", "Automate the Boring Stuff", "Book", "https://automatetheboringstuff.com/", "Yes")
add_resource("UX Design", "Google UX Design Certificate", "Course", "https://www.coursera.org/professional-certificates/google-ux-design", "No")

# View resources
view_resources("Python")
view_resources("UX Design")
"""