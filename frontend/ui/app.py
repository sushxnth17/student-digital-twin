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
    st.write("Simulation started...")
