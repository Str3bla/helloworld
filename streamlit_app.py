import streamlit as st

job_step = st.select_slider(
    "Select a step in the applicant process to ANALYZE",
    options=[
        "Apply",
        "Reviewed",
        "Screen",
        "Interview",
        "Offer",
        "Ready for Hire",
    ],
)
