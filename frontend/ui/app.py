import streamlit as st

# Title
st.title("Student Digital Twin")

# Description
st.write("Frontend interface for the Student Digital Twin system.")

# Input
attendance = st.slider("Attendance (%)", 0, 100, 75)
marks = st.slider("Current Marks (%)", 0, 100, 60)

# Button
if st.button("Run Simulation"):
    if attendance >= 75 and marks >= 60:
        st.success("Predicted Performance: Good")
    elif attendance >= 60:
        st.warning("Predicted Performance: Average")
    else:
        st.error("Predicted Performance: Needs Improvement")



