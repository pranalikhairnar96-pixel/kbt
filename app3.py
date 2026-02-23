import streamlit as st
st.title("Basic Calculator")
num1 = st.number_input("Enter your first number")
num2 = st.number_input("Enter your second number")

Operation = st.selectbox("choose Op",["add","sub","mul","div"])

if st.button("Calculate"):
    if Operation == "add":
        st.write(num1+num2)

    elif Operation == "sub":
        st.write(num1-num2)

    elif Operation == "mul":
        st.write(num1*num2)

    elif Operation == "div":
        if num2!=0:
            st.write(num1/num2)

        else:
            st.write("can not divide by zero")
