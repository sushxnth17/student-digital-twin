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

#Section Box
def section_box(title, subtitle=None):
    st.markdown(f"""
    <div style="
        padding:26px;
        border-radius:26px;
        background:rgba(255,255,255,0.04);
        backdrop-filter: blur(14px);
        border:1px solid rgba(255,255,255,0.08);
        margin-bottom:22px;
    ">
        <div style="font-size:22px;font-weight:700;">{title}</div>
        <div style="opacity:0.7;margin-top:4px;">{subtitle if subtitle else ""}</div>
    </div>
    """, unsafe_allow_html=True)


#Section_Divider
st.markdown("""
<style>

.section-divider{
    height:1px;
    margin:40px 0;
    background:linear-gradient(
        90deg,
        rgba(255,255,255,0),
        rgba(255,255,255,0.15),
        rgba(255,255,255,0)
    );
}

.section-title{
    font-size:22px;
    font-weight:600;
    letter-spacing:.3px;
    margin-bottom:8px;
}

.section-sub{
    opacity:.6;
    margin-bottom:16px;
}

</style>
""", unsafe_allow_html=True)


#Impact CArd
def impact_card(title, before, after, change, impact, percent):

    st.markdown(f"""
    <div class="impact-card">
        <h4>{title}</h4>
        <p>Before: {before} → After: {after}</p>
        <p>Impact: {impact}</p>
        <div class="progress">
            <div class="progress-bar" style="width:{percent}%"></div>
        </div>
        <small>Contribution: {percent:.1f}%</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
.impact-card{
background:rgba(255,255,255,0.03);
padding:20px;
border-radius:18px;
margin-bottom:18px;
backdrop-filter:blur(12px);
border:1px solid rgba(255,255,255,0.08);
}

.progress{
background:rgba(255,255,255,0.05);
height:8px;
border-radius:8px;
overflow:hidden;
margin-top:8px;
}

.progress-bar{
background:linear-gradient(90deg,#22c55e,#38bdf8);
height:100%;
}
</style>
""", unsafe_allow_html=True)

#Glass-Card
st.markdown("""
<style>

.glass-card{
background: rgba(255,255,255,0.06);
border:1px solid rgba(255,255,255,0.08);
backdrop-filter: blur(14px);
border-radius:22px;
padding:24px;
margin-bottom:22px;
}

.big-highlight{
font-size:18px;
font-weight:600;
padding:18px;
border-radius:16px;
background:linear-gradient(90deg, rgba(34,197,94,0.25), rgba(34,197,94,0.45));
border:1px solid rgba(34,197,94,0.5);
}

.impact-item{
padding:14px;
border-radius:14px;
background:rgba(59,130,246,0.12);
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)


#Recommendation_Box
def recommendation_card(message):

    msg = message.lower()

    # detect severity
    if any(word in msg for word in ["urgent","critical","low","poor","improve immediately"]):
        glow = "0 0 30px rgba(239,68,68,0.35)"   # red

    elif any(word in msg for word in ["increase","focus","practice","consider"]):
        glow = "0 0 30px rgba(251,191,36,0.35)"  # yellow

    else:
        glow = "0 0 30px rgba(59,130,246,0.35)"  # blue

    st.markdown(f"""
    <div style="
        padding:18px;
        margin-bottom:14px;
        border-radius:18px;
        background:rgba(255,255,255,0.03);
        backdrop-filter: blur(12px);
        box-shadow:{glow};
    ">
        💡 {message}
    </div>
    """, unsafe_allow_html=True
    )

#State Flag
if "started" not in st.session_state:
    st.session_state.started = False

#PAge State
if "page" not in st.session_state:
    st.session_state.page = "input"

  
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

#REmove Margins
def recommendation_card(message):

    st.markdown(f"""
    <div style="
        padding:18px;
        margin-bottom:14px;
        border-radius:18px;
        background:rgba(255,255,255,0.03);
        backdrop-filter: blur(12px);
        box-shadow:0 0 25px rgba(59,130,246,0.25);
    ">
        💡 {message}
    </div>
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





if st.session_state.page == "input":

    # Input Section
    left, center, right = st.columns([1.1,1,1])

    with center:
        st.markdown("## 🧠 Simulation Setup")
        st.caption("Adjust variables to model your academic twin.")
    
    
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

        st.session_state.inputs = {
            "attendance": attendance,
            "marks": marks,
            "study_hours": study_hours,
            "sleep_hours": sleep_hours,
            "skill_level": skill_level,
            "internship_effort": internship_effort
        }

        #Spinner
        with st.spinner("Simulating your digital twin..."):
            time.sleep(2.5)

        st.session_state.results = run_full_analysis(**st.session_state.inputs)

        st.session_state.page = "results"
        st.rerun()

    


    

if st.session_state.page == "results":


    st.markdown("""
        <div style="
        width:100%;
        margin-left:-20px;
        margin-right:-20px;
        padding:40px 80px;
        border-radius:26px;
        background:linear-gradient(135deg, rgba(56,189,248,0.15), rgba(99,102,241,0.15));
        border:1px solid rgba(56,189,248,0.35);
        margin-bottom:35px;
        backdrop-filter: blur(16px);
        display:flex;
        align-items:center;
        justify-content:space-between;
        ">
        <div>
        <h1 style="margin:0;font-size:38px;">📊 Simulation Results</h1>
        <p style="opacity:0.85;margin-top:6px;font-size:17px;">
        Your digital twin analysis and growth insights.
        </p>
        </div>
        </div>
        """, unsafe_allow_html=True)

    colA, colB = st.columns([8,2])

    with colB:
        if st.button("✏️ Edit Inputs"):
            st.session_state.page = "input"
            st.rerun()

    inputs = st.session_state.inputs
    results = st.session_state.results

    improved_result = run_full_analysis(
    attendance=inputs["attendance"],
    marks=inputs["marks"],
    study_hours=min(inputs["study_hours"] + 2, 12),
    sleep_hours=min(inputs["sleep_hours"] + 1, 10),
    skill_level=min(inputs["skill_level"] + 2, 10),
    internship_effort=min(inputs["internship_effort"] + 1, 10)
)


        
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    
    #Ai Summary
    placement = results["current"]["placement_probability"]
    career = results["current"]["career_score"]
    marks = results["current"]["final_marks"]

    if placement == "High" and career > 75:
        summary = (
            "Strong placement readiness detected. Maintain consistency and focus on real-world project exposure to secure top opportunities."
        )

    elif placement == "Medium" and career >= 65:
        summary = (
            "Your profile shows good potential but lacks consistency. Increasing study discipline and practical experience will significantly boost outcomes."
        )

    elif marks < 60:
        summary = (
            "Academic performance is limiting growth. Prioritize core subjects and structured study routines to stabilize your trajectory."
        )

    else:
        summary = (
            "Your digital twin indicates moderate progress. Small improvements in skills, internships, and study habits can create noticeable gains."
        )
    

    #Current Performance
    section_box("Current Performance",
        "These results represent the student's current academic and career standing "
        "based on input habits and performance indicators."
    )
    
    
    #Key Metrics
    col1, col2, col3 = st.columns(3)

    final_marks = results["current"]["final_marks"]
    career_score = results["current"]["career_score"]
    placement_status = results["current"]["placement_probability"]

    def glow_marks(v):
        if v >= 75: return "rgba(34,197,94,0.55)"
        if v >= 50: return "rgba(251,191,36,0.55)"
        return "rgba(239,68,68,0.55)"

    def glow_career(v):
        if v >= 80: return "rgba(34,197,94,0.55)"
        if v >= 60: return "rgba(251,191,36,0.55)"
        return "rgba(239,68,68,0.55)"

    def glow_place(v):
        if v == "High": return "rgba(34,197,94,0.55)"
        if v == "Medium": return "rgba(251,191,36,0.55)"
        return "rgba(239,68,68,0.55)"

    def metric_card(title, value, glow):
        st.markdown(f"""
        <div style="
            padding:22px;
            border-radius:24px;
            background:rgba(255,255,255,0.05);
            backdrop-filter: blur(12px);
            box-shadow:0 0 35px {glow};
            transition:0.3s;
        ">
            <div style="font-size:14px;opacity:0.7;">{title}</div>
            <div style="font-size:34px;font-weight:700;margin-top:6px;">{value}</div>
        </div>
        """, unsafe_allow_html=True)

    with col1:
        metric_card("Final Marks", final_marks, glow_marks(final_marks))

    with col2:
        metric_card("Career Score", career_score, glow_career(career_score))

    with col3:
        metric_card("Placement Probability", placement_status, glow_place(placement_status))

    
    #Ai Insight
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="
        padding:26px;
        border-radius:24px;
        background:linear-gradient(135deg, rgba(99,102,241,0.18), rgba(59,130,246,0.18));
        backdrop-filter: blur(14px);
        margin-bottom:30px;
        box-shadow:0 0 40px rgba(99,102,241,0.25);
    ">
    <h3>🧠 AI Insight</h3>
    <p>{summary}</p>
    </div>
    """, unsafe_allow_html=True)


   
    # Warnings
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    section_box("Warnings")

    if results["warnings"]:
        for warn in results["warnings"]:
            st.markdown(f'<div class="warning-card">{warn}</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="
            padding:18px;
            border-radius:18px;
            background:rgba(0,255,180,0.08);
            border:1px solid rgba(0,255,180,0.25);
            text-align:center;
            font-size:16px;">
            ✅ Everything looks good. Your digital twin sees no risks right now.
            </div>
        """, unsafe_allow_html=True)



    # Recommendations
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    section_box("Recommendations")

    for rec in results["recommendations"]:
        recommendation_card(rec)


    
    # Scenario Comparison
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    section_box("Scenario Comparison")

    comparison = results["scenario_comparison"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Marks Change",
            f"{comparison['final_marks_change']:.2f}"
        )

        st.metric(
            "Placement Before",
            comparison["placement_probability_before"]
        )

    with col2:
        st.metric(
            "Career Score Change",
            f"{comparison['career_score_change']:.2f}"
        )

        st.metric(
            "Placement After",
            comparison["placement_probability_after"]
        )

    # Impact Breakdown
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    section_box("Impact Breakdown")

    impact = results["impact_breakdown"]

    cols = st.columns(2)

    i = 0
    for factor, data in impact.items():

        with cols[i % 2]:

            percent = data["percentage_contribution"]

            st.markdown(f"""
            <div class="impact-card">

            <h4>{factor.replace('_',' ').title()}</h4>

            <p>
            Before: {data['before']} → After: {data['after']}
            </p>

            <p>
            Estimated Impact: {data['estimated_impact']}
            </p>

            <div class="progress">
                <div class="progress-bar" style="width:{percent}%"></div>
            </div>

            <small>Contribution: {percent:.1f}%</small>

            </div>
            """, unsafe_allow_html=True)

        i += 1
        
    
    # Primary Growth Driver
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    section_box("Primary Growth Driver")
    driver = results["primary_growth_driver"]

    st.markdown(f"""
    <div style="
    padding:22px;
    border-radius:22px;
    background:linear-gradient(135deg, rgba(34,197,94,0.25), rgba(34,197,94,0.05));
    border:1px solid rgba(34,197,94,0.4);
    font-size:18px;
    font-weight:600;
    ">
    🚀 {driver}
    </div>
    """, unsafe_allow_html=True)


    
    # Weekly Progress Chart
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    section_box("Weekly Progress")
    progress = results["progress"]
    df = pd.DataFrame(progress)

    fig = px.line(
        df,
        x="week",
        y="marks",
        markers=True,
        line_shape="spline",
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e6edf7"),
        margin=dict(l=20,r=20,t=20,b=20),
        hovermode="x unified",
        xaxis_title="Week"
 )

    fig.update_traces(
            line=dict(width=4, color="#38bdf8"), 
            marker=dict(size=8, color="#22c55e"))   
    st.markdown("""
        <div style="
        padding:20px;
        border-radius:22px;
        background:rgba(255,255,255,0.03);
        border:1px solid rgba(255,255,255,0.08);
        backdrop-filter:blur(10px);
        ">
        """, unsafe_allow_html=True)

    st.plotly_chart(fig, width="stretch")

    st.markdown("</div>", unsafe_allow_html=True)


    # Contribution Chart
    
    section_box("Factor Contribution Analysis")

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

    chart_df = chart_df.sort_values("Contribution (%)", ascending=False)

    fig2 = px.bar(
        chart_df,
        x="Factor",
        y="Contribution (%)",
        text="Contribution (%)",
        color="Contribution (%)",
        color_continuous_scale="Tealgrn"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e6edf7"),
        margin=dict(l=10, r=10, t=20, b=10),
        coloraxis_showscale=False
    )

    fig2.update_traces(
        marker_line_width=0,
        textposition="outside",
        marker= dict(
            color=values,
            colorscale="Tealgrn",
            )
    )

    st.markdown("""
        <div style="
        padding:20px;
        border-radius:22px;
        background:rgba(255,255,255,0.03);
        border:1px solid rgba(255,255,255,0.08);
        backdrop-filter:blur(10px);
        ">
        """, unsafe_allow_html=True)

    st.plotly_chart(fig2, width="stretch")

    st.markdown("</div>", unsafe_allow_html=True)











