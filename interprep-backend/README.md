# **Interprep – Internship & Employment Preparation Tool**

**Interprep** is an interactive application designed to help **high school and university students** identify, build, and track the skills they need to secure internships or entry-level employment.

This project is currently in its **MVP (Minimum Viable Product)** stage and is being developed in Python with a console-based interface (migrated from Google Colab).

---

## **📌 Purpose**
Interprep helps students:
- Match with relevant career skillsets
- Identify gaps between current abilities and job requirements
- Get tailored learning plans to close those gaps
- Track progress toward career readiness

---

## **🔗 Udemy API (Planned/Optional)**
We plan to integrate the **Udemy API (via RapidAPI or official Affiliate API)** to:
- Search Udemy’s catalog for courses that map to “missing skills”
- Recommend **top-rated** courses (free and paid)
- Present choices alongside other platforms (Coursera, edX, freeCodeCamp)

---

## **🛠 Features (MVP)**
- **User Profile Intake**: name, school, major, project links
- **Resume Parsing (PDF)**: extracts skills from uploaded resume
- **Skills Gap Analysis**: compares resume skills vs. career requirements (from CSV)
- **Learning Resource Suggestions**: maps missing skills to curated resources (CSV; API WIP)
- **Progress Tracker**: update/view completion percentage per skill
- **Roadmap Generator**: prints an ordered learning plan
- **Debugging Tools**: helper to inspect resume text and diagnose matching issues

---

## **📅 Future Features**
- Mentor matching (alumni/pros)
- Job alerts by readiness level
- AI resume critique + keyword optimization
- Mock interview practice (technical/behavioral)
- Web app (Flask/FastAPI/Django) with file uploads
- Fuzzy skill matching + NLP extraction (spaCy/transformers)

---

## **📂 Repository Structure**
```

Interprep/
├─ **pycache**/                             # Python cache (auto-generated)
├─ resumes/                                 # Sample/user resumes (PDFs)
│   └─ \<your\_resume\_files>.pdf
│
├─ Interprep\_MVP.py                         # Core InterprepUser class (I/O, parsing, matching, plan, debug)
├─ Interprep\_demo.py                        # Console demo/runner for the MVP flow
├─ career\_skills\_manager.py                 # Utilities to create/append/update career→skills CSV
├─ learning\_resource\_manager.py             # Utilities to create/append/update skill→resources CSV
├─ udemy\_api\_integration.py                 # (WIP) helpers to fetch courses via Udemy/RapidAPI
│
├─ skills\_database.csv                      # Career → semicolon-separated skills
├─ learning\_resources\_database.csv          # Skill → semicolon-separated resource links/titles
│
├─ requirements.txt                         # Python dependencies (preferred)
├─ requirments.txt                          # Legacy/misspelled file (kept if present)
└─ README.md                                # This documentation

````

---

## **▶️ Quick Start**

### 1) Clone & enter the project
```bash
git clone https://github.com/Murede/Interprep.git
cd Interprep
````

### 2) Create & activate a virtual environment

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
# If your repo only has the legacy file:
# pip install -r requirments.txt
```

### 4) Run the console demo

```bash
python Interprep_demo.py
```

You’ll be prompted for basic info, a **career** (must match a key in `skills_database.csv`, e.g., “Software Engineer” or “Electrical Engineer”), and the **path to your resume PDF**.

> **Windows tip:** If you paste a path that includes quotes, the app strips them automatically.
> Example path (no quotes):
> `C:\Users\YourName\Documents\Interprep\resumes\My Resume.pdf`

---

## **🧪 What the Demo Does**

1. Collects your profile details
2. Reads your resume PDF and extracts text
3. Loads required skills for your chosen career from `skills_database.csv`
4. Detects which of those skills appear in your resume
5. Shows **Matched** vs **Missing** skills
6. Prints recommended learning resources (from `learning_resources_database.csv`)
7. Generates a simple step-by-step learning plan
8. Demonstrates the skill progress tracker

---

## **🔎 Debugging Resume Parsing**

If skills aren’t being detected:

* Use the built-in debug helper (called inside the demo) to:

  * Preview the first chunk of extracted resume text
  * Verify your **career key** exists in the CSV
  * See which skills are expected and which matched
* Common issues:

  * **Scanned PDFs** (no real text): use OCR or export a text-based PDF
  * **Career key mismatch** (“Electrical Engineering” vs “Electrical Engineer”)
  * **Wording variance** (“MATLAB” vs “Matlab”); fuzzy matching will be added next

---

## **🧱 Data Files**

* **`skills_database.csv`**

  ```
  Career,Skills
  Software Engineer,Python;Java;C++;Data Structures;Algorithms;Git;SQL;Agile Development
  Electrical Engineer,Circuit Design;MATLAB;Power Systems;PCB Design;Microcontrollers;AutoCAD Electrical
  ...
  ```
* **`learning_resources_database.csv`**

  ```
  Skill,Resources
  Python,Automate the Boring Stuff;Python for Everybody;CS50P;...
  MATLAB,MathWorks Onramp;Coursera MATLAB;YouTube MATLAB Tutorials;...
  ...
  ```

---

## **🔗 (Optional) Udemy API Set-up**

* Official Udemy Affiliate API calls may block shared/cloud IPs; you can:

  * Run from your local machine/server, **or**
  * Use **RapidAPI’s Udemy wrapper** (paid tiers for steady usage)
* Store credentials as environment variables and call via `udemy_api_integration.py`

---

## **🤝 Contributing**

PRs are welcome!

* Keep CSVs clean and consistent (exact career keys, semicolon-separated skills)
* Add tests or sample resumes if possible

---

## **📜 License**

MIT License.

---

## **📧 Contact**

**Developer**: Murede Adetiba
**Email**: [murede2005@gmail.com](mailto:your-email@example.com)
**GitHub**: [https://github.com/Murede](https://github.com/Murede)


