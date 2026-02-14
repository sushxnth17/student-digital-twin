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

    results = run_full_analysis(
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


    st.metric(
        "Final Marks",
        results["current"]["final_marks"]
    )

    st.metric(
        "Career Score",
        results["current"]["career_score"]
    )

    st.metric(
        "Placement Probability",
        results["current"]["placement_probability"]
)


   
    # Warnings
    st.divider()
    st.subheader("Warnings")

    if results["warnings"]:
        for warn in results["warnings"]:
            st.warning(warn)
    else:
        st.success("No critical warnings detected.")



    # Recommendations
    st.divider()
    st.subheader("Recommendations")

    for rec in results["recommendations"]:
        st.write("•", rec)


    
    
    
    # Scenario Comparison
    st.divider()
    st.subheader("Scenario Comparison")

    comparison = results["scenario_comparison"]

    st.metric(
        "Marks Change",
        f"{comparison['final_marks_change']:.2f}"
    )

    st.metric(
        "Career Score Change",
        f"{comparison['career_score_change']:.2f}"
    )

    st.metric(
        "Placement Before",
        comparison["placement_probability_before"]
    )

    st.metric(
        "Placement After",
        comparison["placement_probability_after"]
    )



    #Impact Breakdown
    st.divider()
    st.subheader("Impact Breakdown")

    impact = results["impact_breakdown"]

    for factor, data in impact.items():
        st.write(f"**{factor.replace('_',' ').title()}**")
        st.write(f"Before: {data['before']}")
        st.write(f"After: {data['after']}")
        st.write(f"Change: {data['change']}")
        st.write(f"Estimated Impact: {data['estimated_impact']}")
        st.write(f"Contribution: {data['percentage_contribution']}%")
        st.divider()









