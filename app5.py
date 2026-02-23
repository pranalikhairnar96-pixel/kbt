import streamlit as st

st.markdown("""
<style>
            .stButton > button
            {
            background-color:green;
            color:white;
            border-radius:50%;         
           }
</style>



""",unsafe_allow_html=True)



st.title("Welcome To Basic Streamlit App")

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city",["Delhi","mumbai","nashik","pune"])
str1 = st.text_input("Enter your first name")
str2 = st.text_input("Enter your last name")
date = st.date_input("Enter your birthdate")
if st.button("show details"):
    st.write("age",age)
    st.write("city",city)
    st.write("First name:",str1)
    st.write("Last name:",str2)
    st.write("date of Birth",date)