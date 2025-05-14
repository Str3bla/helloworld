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

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite Job Step?',
    ('Apply','Reviewed','Screen','Interview','Offer','Ready for Hire'))

st.write('Your favorite job step is ', option)


st.write("Segmented Trending by ", job_step)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
