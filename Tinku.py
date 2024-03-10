import streamlit as st
import pandas as pd

a = pd.read_csv("Book1.csv")

st.dataframe(a)

a = st.text_input("enter your email")
b = st.text_input("enter your password for comform")

button = st.button("done")
if button:
    st.markdown(f"""
    email : {a}
    password : {b}
    """)