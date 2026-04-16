# 📘🧠 MirrorMind — Student Digital Twin

Status: Completed

MirrorMind is a compact, explainable simulator that shows how daily habits influence long-term academic outcomes and placement readiness.

The project prioritizes transparent, rule-based reasoning over black-box ML, making outputs actionable for educators and learners.

---

## 🚀 At a Glance

MirrorMind uses a few core behavioral and academic inputs to produce clear, interpretable outcomes:

- Attendance
- Current marks
- Daily study hours
- Sleep hours
- Skill level
- Internship effort

Outputs include:

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

Instead of explaining what happened, MirrorMind answers: “If a student improves X today, how will outcomes change?”

It runs a lightweight time-lag simulation with weighted contribution rules so you can see how habit changes propagate into marks and career readiness.

---

## 🏗️ Architecture Overview

### 🔹 Backend (Python)

Located in `/backend`. Key modules:

- `data.py` — student model and validators
- `logic.py` — contribution rules
- `simulation.py` — progression engine (weekly steps)
- `career.py` — career-readiness scoring
- `recommendations.py` — suggestion generator
- `scenario.py` — comparator for current vs improved scenarios
- `service.py` — orchestration and analysis API
- `app.py` — lightweight runner for quick tests

Quick example:

```python
from backend.service import run_full_analysis

# run_full_analysis(input_dict) -> full analysis report
```

### 🔹 Frontend (Streamlit)

The interactive UI is in `/frontend`.

- Collects habit inputs via sliders
- Runs simulations on demand
- Visualizes projections, scenario deltas, and per-factor impacts

Key features:

1. Weekly academic projections driven by habit inputs
2. Career analytics combining consistency, skill growth, and internship effort
3. Scenario comparison with clear delta summaries
4. Explainable impact breakdowns showing percent contribution and primary drivers

---

## 🛠️ Quick Start

1. Clone the repo

```bash
git clone <repo-url>
cd student-digital-twin
```

2. Create a virtual environment and install dependencies

Cross-platform (Windows PowerShell shown):

```bash
python -m venv .venv
# Activate (PowerShell)
.\.venv\Scripts\Activate.ps1
# On macOS / Linux
# source .venv/bin/activate
pip install -r requirements.txt
```

3. Run backend (test mode)

```bash
python -m backend.app
```

4. Launch the Streamlit UI

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
- Expose a REST API (FastAPI)
- Richer visualizations and trend analytics
- Deploy to a hosting platform (Streamlit Cloud / Docker)

---

## 👥 Contributors

- Backend: Sushanth S
- Frontend: Vishal S Naik

---

## 🌐 Live Demo

Try the live prototype: https://mirroredminds.streamlit.app/

