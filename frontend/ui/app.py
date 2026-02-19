import sys
import os

import pandas as pd


sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

from backend.service import run_full_analysis
import streamlit as st

# Title and Description
#st.title("Student Digital Twin")
#st.write("Frontend interface for the Student Digital Twin system.")

#st.divider()

st.set_page_config(
    page_title="MirrorMind",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Logo
col1, col2, col3 = st.columns([1,1.5,1])

with col2:
    st.markdown("""
        <div style="display:flex; justify-content:center;">
            <img src="data:image/png;base64,{img}" 
            style="
                width:160px;
                height:160px;
                border-radius:50%;
                object-fit:cover;
                box-shadow:0 10px 30px rgba(0,0,0,0.5);
            ">
        </div>
    """.format(img=img_to_base64("frontend/ui/assets/logo.png")),
    unsafe_allow_html=True)




#Hero Section

st.markdown("""
<style>
.hero-wrapper{
    display:flex;
    justify-content:center;
    align-items:center;
    width:100%;
    margin-top:20px;
}

.hero-card{
    text-align:center;
    padding:34px;
    width:520px;
    border-radius:24px;
    background:linear-gradient(180deg,#0f172a,#020617);
    box-shadow:0 30px 80px rgba(0,0,0,0.7);
}
.hero-title{
    margin:0;
    font-size:46px;
    font-weight:800;
}
.hero-sub{
    color:#9ca3af;
    font-size:16px;
    margin-top:6px;
}
</style>

<div class="hero-wrapper">
<div class="hero-card">
<h1 class="hero-title">MirrorMind</h1>
<p class="hero-sub">Student Digital Twin System</p>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)



# Input Section
st.divider()
st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
left, center, right = st.columns([1.1,1,1])

with center:
    st.markdown("## Student Input Parameters")

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.divider()

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.markdown("### 🎓 Academic Performance")

attendance = st.slider("Attendance (%)", 0, 100, 75)
marks = st.slider("Current Marks (%)", 0, 100, 60)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

st.divider()

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.markdown("### 🕒 Lifestyle Habits")

study_hours = st.slider("Daily Study Hours", 0, 12, 2)
sleep_hours = st.slider("Daily Sleep Hours", 0, 12, 6)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.divider()

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

st.markdown("### 🚀 Career Development")
skill_level = st.slider("Skill Level (0–10)", 0, 10, 3)
internship_effort = st.slider("Internship Effort (0–10)", 0, 10, 2)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.divider()

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
        
    
    # Primary Growth Driver
    st.divider()
    st.subheader("Primary Growth Driver")

    st.success(results["primary_growth_driver"])


    
    # Weekly Progress Chart
    st.divider()
    st.subheader("Weekly Progress")
    progress = results["progress"]
    df = pd.DataFrame(progress)
    st.line_chart(df.set_index("week")["marks"])



    # Contribution Chart
    st.divider()
    st.subheader("Factor Contribution Analysis")

    impact = results["impact_breakdown"]

    labels = []
    values = []

    for factor, data in impact.items():
        labels.append(factor.replace("_", " ").title())
        values.append(data["percentage_contribution"])

    chart_df = pd.DataFrame({
        "Factor": labels,
        "Contribution (%)": values
    })

    st.bar_chart(chart_df.set_index("Factor"))











