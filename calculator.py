import streamlit as st
st.title("Welcome to Calculator")
st.header("Obaid ud din Hashmi")
a = st.number_input("Enter 1st Number: ")
b = st.number_input("Enter 2nd Number: ")
status = st.radio("Enter operator: ",
         ['addition','subtraction','multiplication','division'])
if(st.button('Answer')):
    try:
        if status == "addition":
            st.text(f"your answer is: {a+b}")
        elif status == "subtraction":
            st.text(f"your answer is: {a-b}")
        elif status == "multiplication":
            st.text(f"your answer is: {a*b}")
        else:
            st.text(f"your answer is: {a/b}")
    except:
        st.text("Select operator")
