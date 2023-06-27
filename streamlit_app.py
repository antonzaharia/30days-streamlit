import streamlit as st

st.header("st.button")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Click"):
    st.write("Clicked")
else:
    st.write("Not clicked")

st.button("Nothing")