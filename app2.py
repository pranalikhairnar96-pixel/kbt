import streamlit as st
st.title("Welcome To Basic Streamlit App")

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city",["Delhi","mumbai","nashik","pune"])

if st.button("show details"):
    st.write("age",age)
    st.write("city",city)