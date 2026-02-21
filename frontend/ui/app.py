import sys
import os

import pandas as pd

import plotly.express as px


sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

from backend.service import run_full_analysis
import streamlit as st


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


#State Flag
if "started" not in st.session_state:
    st.session_state.started = False

  
#BackGround Colour
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top,
    #0f172a,
    #020617 60%,
    #010409);
}

</style>
""", unsafe_allow_html=True)



#Slider Glow
st.markdown("""
<style>

/* Hide slider tooltip */
[data-baseweb="tooltip"]{
    display:none !important;
}

/* Slider value number */
.stSlider [data-baseweb="slider"] span {
    color: white !important;
    font-weight: 600 !important;
}

/* track */
.stSlider > div > div{
    background:#1e293b;
    height:6px;
    border-radius:10px;
}

/* filled */
.stSlider [data-baseweb="slider"] div div{
    background:#38bdf8;
}

/* thumb */
.stSlider [data-baseweb="slider"] div[role="slider"]{
    width:14px;
    height:14px;
    border-radius:50%;
    background:#38bdf8;
    box-shadow:0 0 6px rgba(56,189,248,0.35);
}

/* remove scaling */
.stSlider [data-baseweb="slider"]:hover div{
    transform:none;
}

</style>
""", unsafe_allow_html=True)

#Section Card Style
st.markdown("""
<style>
.section-card{
background: rgba(255,255,255,0.1);
border:1px solid rgba(255,255,255,0.08);
backdrop-filter: blur(12px);
border-radius:18px;
padding:24px;
margin-top:20px;
margin-bottom:30px;
}
</style>
""", unsafe_allow_html=True)

#Run Button Style
st.markdown("""
<style>

/* Run Simulation Button */
div.stButton > button {
    background: linear-gradient(135deg,#1e293b,#334155);
    color:white;
    border-radius:12px;
    padding:10px 20px;
    border:1px solid rgba(255,255,255,0.1);
    font-weight:600;
    transition: all 0.25s ease;
}

/* Hover effect */
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:0 8px 25px rgba(56,189,248,0.5);
    border:1px solid rgba(56,189,248,0.4);
}

</style>
""", unsafe_allow_html=True)

#Metric Cards
st.markdown("""
<style>

/* Metric Cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.1);
    padding:20px;
    border-radius:24px;
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(6px);
}

</style>
""", unsafe_allow_html=True)

#Warning Cards
st.markdown("""
<style>

.warning-card{
    padding:18px;
    border-radius:14px;
    background: linear-gradient(90deg, rgba(255,215,0,0.25), rgba(255,215,0,0.5));
    border:1px solid rgba(255,215,0,0.5);
    margin-bottom:12px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

#Recomendations cards
st.markdown("""
<style>
.reco-card{
    padding:16px;
    border-radius:14px;
    background: rgba(56,189,248,0.1);
    border:1px solid rgba(56,189,248,0.25);
    margin-bottom:10px;
    font-size:15px;
}
</style>
""", unsafe_allow_html=True)


#Section Spacing
st.markdown("""
<style>

/* Section spacing */
section.main > div {
    padding-top: 2rem;
}

/* Space between blocks */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Divider styling */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg,transparent,#1f2a44,transparent);
    margin: 40px 0;
}

</style>
""", unsafe_allow_html=True)


#Chart Styling
st.markdown("""
<style>

/* Chart container glass effect */
.stPlotlyChart, canvas {
    border-radius:18px;
    background:rgba(255,255,255,0.02);
    padding:10px;
}

/* Axis text softer */
svg text {
    fill:#9fb0d1 !important;
    font-size:12px;
}

/* Grid softer */
svg line {
    stroke:#1f2a44 !important;
}

</style>
""", unsafe_allow_html=True)




#Welcome Screen Layout
if not st.session_state.started:

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

    

    #Lets Begin Button
    st.markdown("""
    <div style="
        text-align:center;
        padding:60px 20px;
        max-width:750px;
        margin:auto;
        background:rgba(255,255,255,0.03);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:20px;
        backdrop-filter:blur(10px);
    ">
        <h1 style="margin-bottom:10px;">Student Digital Twin</h1>
        <p style="opacity:0.8;font-size:16px;">
        Simulate academic growth, identify key drivers, and predict placement readiness
        using an explainable digital twin model.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        if st.button("🚀 Let's Begin", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.stop()


# Input Section
left, center, right = st.columns([1.1,1,1])

with center:
    st.markdown("## Student Input Parameters")



#Academic Performance
st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)


st.markdown("""
<h3 style="
display:flex;
align-items:center;
gap:10px;
margin-bottom:10px;
">
🎓 <span style="font-weight:700;">Academic Performance</span>
</h3>
""", unsafe_allow_html=True)


attendance = st.slider("Attendance (%)", 0, 100, 75)
st.caption(f"Value: {attendance}%")
st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
marks = st.slider("Current Marks (%)", 0, 100, 60)
st.caption(f"Value: {marks}%")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


# Lifestyle Habits
st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.markdown("""
<h3 style="
display:flex;
align-items:center;
gap:10px;
margin-bottom:10px;
">
🕒 <span style="font-weight:700;">Lifestyle Habits</span>
</h3>
""", unsafe_allow_html=True)


study_hours = st.slider("Daily Study Hours", 0, 12, 2)
st.caption(f"Value: {study_hours} hours")
st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
sleep_hours = st.slider("Daily Sleep Hours", 0, 12, 6)
st.caption(f"Value: {sleep_hours} hours")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


# Career Development
st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.markdown("""
<h3 style="
display:flex;
align-items:center;
gap:10px;
margin-bottom:10px;
">
🚀 <span style="font-weight:700;">Career Development</span>
</h3>
""", unsafe_allow_html=True)

skill_level = st.slider("Skill Level (0–10)", 0, 10, 3)
st.caption(f"Value: {skill_level}/10")
st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)
internship_effort = st.slider("Internship Effort (0–10)", 0, 10, 2)
st.caption(f"Value: {internship_effort}/10")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)


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


    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Current Performance")
    st.caption(
        "These results represent the student's current academic and career standing "
        "based on input habits and performance indicators."
    )


    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Final Marks",
            results["current"]["final_marks"]
        )

    with col2:
        st.metric(
            "Career Score",
            results["current"]["career_score"]
        )

    with col3:
        st.metric(
            "Placement Probability",
             results['current']['placement_probability']
    )


   
    # Warnings
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Warnings")

    if results["warnings"]:
        for warn in results["warnings"]:
            st.markdown(f'<div class="warning-card">{warn}</div>', unsafe_allow_html=True)
    else:
        st.success("No critical warnings detected.")



    # Recommendations
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Recommendations")

    for rec in results["recommendations"]:
        st.markdown(f'<div class="reco-card">💡 {rec}</div>', unsafe_allow_html=True)


    
    # Scenario Comparison
    st.markdown("<hr>", unsafe_allow_html=True)
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
    st.markdown("<hr>", unsafe_allow_html=True)
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
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Primary Growth Driver")
    st.success(results["primary_growth_driver"])


    
    # Weekly Progress Chart
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Weekly Progress")
    progress = results["progress"]
    df = pd.DataFrame(progress)

    fig = px.line(
        df,
        x="week",
        y="marks",
        markers=True
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e6edf7"),
        margin=dict(l=20,r=20,t=20,b=20)
    )

    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)



    # Contribution Chart
    st.markdown("<hr>", unsafe_allow_html=True)
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

    fig2 = px.bar(
        chart_df,
        x="Factor",
        y="Contribution (%)",
        text="Contribution (%)"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e6edf7"),
        margin=dict(l=20, r=20, t=20, b=20)
    )

    fig2.update_traces(
        marker_line_width=0,
        textposition="outside"
    )

    st.plotly_chart(fig2, use_container_width=True)











