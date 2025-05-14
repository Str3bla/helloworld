import streamlit as st
import pandas as pd
import numpy as np

st.write("Segmented Trending by ", job_step)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("")
st.write("")
st.write("")

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.write("")
st.write("")
st.write("")

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.sidebar.write('Selected number from slider widget is:', number)

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

st.sidebar.write("")

option = st.selectbox(
    'What do you want to compare it to?',
    ('Rejected/Declined','Apply','Reviewed','Screen','Interview','Offer','Ready for Hire'))

st.write("")

option1 = st.multiselect(
    'What Business Units?',
    ['Finance','Marketing','HR','Operations','Product','Sales'])

st.write("")

st.write('What challenges do you want TA GPT to help with?')

Scenario_TTF = st.checkbox("Time to Fill")
Scenario_Difficulty = st.checkbox("Location")
Scenario_Conversion = st.checkbox("Conversion")
Scenario_Quantity = st.checkbox("Compensation")
