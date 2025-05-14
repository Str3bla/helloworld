import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

st.header('write')

# Example 1

st.write('Hello *World* :sungalsses:')

# Example 2
st.write(1234)

# Example 3

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.write(df)

# Example 4

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a','b','c'])

st.write(c)