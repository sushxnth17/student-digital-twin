import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

from backend.service import run_full_analysis
import streamlit as st

# Title and Description
st.title("Student Digital Twin")
st.write("Frontend interface for the Student Digital Twin system.")

st.divider()

# Input Section
st.subheader("Student Input Parameters")


attendance = st.slider("Attendance (%)", 0, 100, 75)
marks = st.slider("Current Marks (%)", 0, 100, 60)
study_hours = st.slider("Daily Study Hours", 0, 12, 2)
sleep_hours = st.slider("Daily Sleep Hours", 0, 12, 6)
skill_level = st.slider("Skill Level (0–10)", 0, 10, 3)
internship_effort = st.slider("Internship Effort (0–10)", 0, 10, 2)

st.caption(
    "Adjust the sliders to simulate different academic and lifestyle scenarios."
)


# Run Simulation Button

if st.button("Run Simulation"):

    result = run_full_analysis(
        attendance=attendance,
        marks=marks,
        study_hours=study_hours,
        sleep_hours=sleep_hours,
        skill_level=skill_level,
        internship_effort=internship_effort
    )

    improved_result = run_full_analysis(
        attendance=attendance,
        marks=marks,
        study_hours=min(study_hours + 2, 12),
        sleep_hours=min(sleep_hours + 1, 10),
        skill_level=min(skill_level + 2, 10),
        internship_effort=min(internship_effort + 1, 10)
    )


    st.divider()

    st.subheader("Current Performance")
    st.caption(
        "These results represent the student's current academic and career standing "
        "based on input habits and performance indicators."
    )

    st.metric("Final Marks", result["current"]["final_marks"])
    st.metric("Career Score", result["current"]["career_score"])
    st.metric("Placement Probability", result["current"]["placement_probability"])

    # Warnings
    if result.get("warnings"):
        st.divider()
        st.subheader("Warnings")
        for w in result["warnings"]:
            st.warning(w)
    else:
        st.divider()
        st.subheader("Warnings")
        st.success("No critical warnings detected.")



    # Recommendations
    if result.get("recommendations"):
        st.divider()
        st.subheader("Recommendations")
        for r in result["recommendations"]:
            st.success(r)
    
    
    #Scenario Comparison
    st.divider()
    st.subheader("Scenario Comparison")

    st.write("Current Habits Performance")
    st.metric(
        "Career Score (Current)",
        result["current"]["career_score"]
    )

    st.metric(
        "Placement Probability (Current)",
        result["current"]["placement_probability"]
    )

    st.divider()

    st.write("Improved Habits Performance")
    st.metric(
        "Career Score (Improved)",
        improved_result["current"]["career_score"]
    )

    st.metric(
        "Placement Probability (Improved)",
        improved_result["current"]["placement_probability"]
    )









