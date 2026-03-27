# 📘 MirrorMind - Student Digital Twin System

A simulation-based academic and career analytics system that models how daily student habits influence long-term academic performance and placement readiness.

This project focuses on **explainable logic-based modeling** instead of black-box machine learning.

---

## 🚀 Project Overview

The Student Digital Twin models a student using behavioral and academic inputs such as:

- Attendance
- Current Marks
- Daily Study Hours
- Sleep Hours
- Skill Level
- Internship Effort

It simulates academic progress over time and generates:

- 📊 Final Marks Prediction  
- 🎯 Career Readiness Score  
- 💼 Placement Probability  
- 🔄 Scenario Comparison (Current vs Improved Habits)  
- 🧠 Explainable Impact Breakdown  
- 📈 Primary Growth Driver Analysis  
- 💡 Personalized Recommendations  
- ⚠️ Input Validation Warnings  

---

## 🧠 Core Idea

Traditional academic systems evaluate only past marks and attendance.

This system answers:

> “How will today’s habits affect future academic and career outcomes?”

The project uses:

- Time-lag simulation modeling  
- Weighted contribution logic  
- Scenario-based improvement comparison  
- Explainable factor-level impact analysis  

---

## 🏗️ System Architecture

### 🔹 Backend (Python Package)

Located inside `/backend`

Modules:

- `data.py` → Student data model  
- `logic.py` → Academic performance logic  
- `simulation.py` → Weekly academic progression engine  
- `career.py` → Career readiness computation  
- `recommendations.py` → Personalized suggestions  
- `scenario.py` → Current vs Improved comparison  
- `service.py` → Unified analysis service layer  
- `app.py` → Backend test runner  

Main entry function:

```python
from backend.service import run_full_analysis
```
###🔹 Frontend (Streamlit)

Interactive interface that:
Accepts habit inputs through sliders
Runs simulation
Displays performance results
Shows scenario comparison
Presents explainable improvement breakdown

📊 Key Features
1️⃣ Academic Progress Simulation

    Simulates marks progression over multiple weeks using habit-based logic.

2️⃣ Career Analytics Engine

    Computes career score using:

        Consistency
        Skill development
        Internship effort

3️⃣ Scenario Comparison

    Compares:

        Current habits
        Improved habits
    Outputs:

        Marks change
        Career score change
        Placement probability shift

4️⃣ Explainable Impact Breakdown

    Each improvement shows:

        Before value
        After value
        Change
        Estimated weighted impact
        Percentage contribution
        Primary growth driver

### 🛠️ Installation & Setup
1.Clone Repository
2.Install dependencies:
    pip install -r requirements.txt
3.Run backend(Testing mode):
    python -m backend.app
4.Run frontend:
    streamlit run frontend/app.py

📦 Tech Stack

    Python
    Streamlit
    Modular Backend Architecture
    Scenario-Based Simulation Engine

🎯 Future Enhancements

    User authentication system
    Database integration (PostgreSQL / SQLite)
    REST API layer using FastAPI
    Advanced dashboard analytics
    Habit trend visualization charts
    Deployment on Streamlit Cloud
    Multi-user support

👨‍💻 Contributors

Backend Development: Sushanth S
Frontend Development: Vishal S Naik

## 🌐 Live Demo

Try the app here: https://mirroredminds.streamlit.app/