import pandas as pd
import streamlit as st

st.header('Displaying DataFrames')

data = pd.DataFrame({
    'Name': ['Alice', 'Michael', 'Andy'],
    'Age': [20, 58, 13],
    'City': ['New York', 'Miami', 'London']
})

st.dataframe(data)

