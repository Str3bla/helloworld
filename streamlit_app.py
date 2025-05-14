import streamlit as st

job_step = st.select_slider(
    "Select a step of the applicant process",
    options=[
        "Apply",
        "Reviewed",
        "Screen",
        "Interview",
        "Offer",
        "Ready for Hire",
    ],
)
st.write("Selected Job Step:", job_step)
