import streamlit as st

# Title of the app
st.title("Calculator")

# Display area
display = st.empty()
display.markdown("<div style='font-size: 40px; color: #333;'>0</div>", unsafe_allow_html=True)

# Session state
if "input_value" not in st.session_state:
    st.session_state.input_value = ""
if "operation" not in st.session_state:
    st.session_state.operation = None

# Functions
def update_display(value):
    st.session_state.input_value += value
    display.markdown(f"<div style='font-size: 40px; color: #333;'>{st.session_state.input_value}</div>", unsafe_allow_html=True)

def set_operation(op):
    if st.session_state.input_value:
        st.session_state.operation = op
        st.session_state.stored_value = st.session_state.input_value
        st.session_state.input_value = ""
        display.markdown("<div style='font-size: 40px; color: #333;'>0</div>", unsafe_allow_html=True)

def calculate_result():
    if st.session_state.operation and st.session_state.input_value:
        num1 = float(st.session_state.stored_value)
        num2 = float(st.session_state.input_value)
        if st.session_state.operation == "Addition":
            result = num1 + num2
        elif st.session_state.operation == "Subtraction":
            result = num1 - num2
        elif st.session_state.operation == "Multiplication":
            result = num1 * num2
        elif st.session_state.operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error"
        st.session_state.input_value = str(result)
        display.markdown(f"<div style='font-size: 40px; color: #333;'>{result}</div>", unsafe_allow_html=True)
        st.session_state.operation = None
        st.balloons()

def clear_input():
    st.session_state.input_value = ""
    display.markdown("<div style='font-size: 40px; color: #333;'>0</div>", unsafe_allow_html=True)

# Styling
button_style = """
    <style>
    .stButton>button {
        font-size: 30px;
        padding: 10px;
        width: 100%;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        color: #333;
    }
    .stButton>button:hover {
        background-color: #ddd;
        border: 1px solid #bbb;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7"): update_display("7")
    if st.button("4"): update_display("4")
    if st.button("1"): update_display("1")
    if st.button("0"): update_display("0")

with col2:
    if st.button("8"): update_display("8")
    if st.button("5"): update_display("5")
    if st.button("2"): update_display("2")
    if st.button("."): update_display(".")

with col3:
    if st.button("9"): update_display("9")
    if st.button("6"): update_display("6")
    if st.button("3"): update_display("3")
    if st.button("="): calculate_result()

with col4:
    if st.button(".+"): set_operation("Addition")
    if st.button(".-"): set_operation("Subtraction")
    if st.button(".*"): set_operation("Multiplication")
    if st.button("/"): set_operation("Division")
    if st.button("C"): clear_input()
