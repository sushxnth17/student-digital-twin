import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

from backend.service import run_full_analysis


import streamlit as st

# Title
st.title("Student Digital Twin")

# Description
st.write("Frontend interface for the Student Digital Twin system.")

# Input
attendance = st.slider("Attendance (%)", 0, 100, 75)
marks = st.slider("Current Marks (%)", 0, 100, 60)
study_hours = st.slider("Daily Study Hours", 0, 12, 2)
sleep_hours = st.slider("Daily Sleep Hours", 0, 12, 6)
skill_level = st.slider("Skill Level (0–10)", 0, 10, 3)
internship_effort = st.slider("Internship Effort (0–10)", 0, 10, 2)


# Button
# NOTE:
# Currently using simple rule-based logic for prediction.
# Backend integration will be added in the next phase
# to provide detailed analytics and recommendations.

if st.button("Run Simulation"):

    result = run_full_analysis(
        attendance=attendance,
        marks=marks,
        study_hours=study_hours,
        sleep_hours=sleep_hours,
        skill_level=skill_level,
        internship_effort=internship_effort
    )

    st.subheader("Current Performance")

    st.metric("Final Marks", result["current"]["final_marks"])
    st.metric("Career Score", result["current"]["career_score"])
    st.metric("Placement Probability",result["current"]["placement_probability"])







