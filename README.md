# 📘🧠 MirrorMind — Student Digital Twin

Current status: completed

A compact, explainable simulation that models how a student's daily habits shape long-term academic performance and placement readiness.

This project emphasizes transparent, rule-based reasoning rather than black-box ML — ideal for educators and learners who want actionable, interpretable insights.

---

## 🚀 At a Glance

MirrorMind models a student using a small set of behavioral and academic inputs:

- Attendance
- Current marks
- Daily study hours
- Sleep hours
- Skill level
- Internship effort

From these, it produces:

- 📊 Final marks prediction
- 🎯 Career readiness score
- 💼 Placement probability
- 🔄 Scenario comparison (current vs improved habits)
- 🧠 Explainable impact breakdown (factor-level)
- 📈 Primary growth driver analysis
- 💡 Personalized, prioritized recommendations
- ⚠️ Input validation and sanity checks

---

## 🧠 Core Idea

Most academic tools look backward. MirrorMind asks:

“If a student improves X today, how does that change outcomes in the future?”

It uses lightweight time-lag simulation and weighted-contribution rules to show how habit changes propagate into marks and career readiness.

---

## 🏗️ Architecture Overview

### 🔹 Backend (Python)

Found under `/backend`. Key modules:

- `data.py` — student data model and validators
- `logic.py` — core contribution rules
- `simulation.py` — progression engine (weekly steps)
- `career.py` — career-readiness scoring
- `recommendations.py` — suggestion generator
- `scenario.py` — current vs improved scenario comparator
- `service.py` — orchestration and analysis API
- `app.py` — lightweight test runner

Entry point example:

```python
from backend.service import run_full_analysis

# use run_full_analysis(input_dict) to get a full report
```

### 🔹 Frontend (Streamlit)

Simple interactive UI lives in `/frontend` and:`

- collects habit inputs via sliders
- runs the simulation
- visualizes predictions, scenario diffs, and impact breakdowns

Key features

1) Academic progress simulation — weekly projections driven by habit inputs

2) Career analytics — scores computed from consistency, skill growth and internship effort

3) Scenario comparison — side-by-side before/after snapshots and delta summaries

4) Explainable impact breakdown — per-factor contribution, percent shares, and primary drivers

---

## 🛠️ Quick Start

1. Clone the repository

```bash
git clone <repo-url>
cd student-digital-twin
```

2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
.\
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# then
pip install -r requirements.txt
```

3. Run the backend (test mode)

```bash
python -m backend.app
```

4. Run the Streamlit frontend

```bash
streamlit run frontend/app.py
```

---

## 📦 Tech Stack

- Python 3.10+
- Streamlit (frontend)
- Modular, testable backend components

---

## 🎯 Roadmap Ideas

- Add authentication and per-user persistence
- Persist experiments and results to a database (SQLite / PostgreSQL)
- Expose a REST API with FastAPI
- Richer visualizations and habit-trend analytics
- Deploy on Streamlit Cloud or a container platform

---

## 👥 Contributors

- Backend: Sushanth S
- Frontend: Vishal S Naik

---

## 🌐 Live Demo

Try the live prototype: https://mirroredminds.streamlit.app/

If you want, I can also: add a short usage example, create badges, or extract a one-page quickstart. Tell me which next step you prefer.