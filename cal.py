import streamlit as st

# Page setup
st.set_page_config(page_title="Ultimate Calculator", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧮 Streamlit Calculator Made by Obaid Hashmi</h1>", unsafe_allow_html=True)

# Session state for the expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to evaluate or modify expression
def handle_input(char):
    if char == "=":
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
    elif char == "C":
        st.session_state.expression = ""
    else:
        st.session_state.expression += char

# Expression input (keyboard friendly)
expression = st.text_input("Enter expression", value=st.session_state.expression, key="input_field")

# Update expression from keyboard input
if expression != st.session_state.expression:
    st.session_state.expression = expression

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "X"],
    ["1", "2", "3", ".-"],
    ["0", "C", "=", ".+"]
]

st.markdown("### Click buttons below 👇 or type with keyboard:")

# Render buttons
for row in buttons:
    cols = st.columns(4)
    for i, char in enumerate(row):
        if cols[i].button(char, use_container_width=True):
            handle_input(char)

# Final result display (optional)
if st.session_state.expression:
    try:
        result = eval(st.session_state.expression)
        st.success(f"Result: {result}")
    except:
        pass  # Invalid intermediate expression
