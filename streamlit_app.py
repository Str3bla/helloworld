import streamlit as st
import pandas as pd
import numpy as np

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

st.write(' ')

option = st.selectbox(
    'What do you want to compare it to?',
    ('Rejected/Declined','Apply','Reviewed','Screen','Interview','Offer','Ready for Hire'))

st.write(' ')

option1 = st.multiselect(
    'What Business Units?',
    ['Finance','Marketing','HR','Operations','Product','Sales'])

st.write(' ')

st.write("Segmented Trending by ", job_step)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
