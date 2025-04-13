
import streamlit as st
import re
from math import sqrt, pow

# Initialize session state variables
if 'current_input' not in st.session_state:
    st.session_state.current_input = '0'
if 'calculation_done' not in st.session_state:
    st.session_state.calculation_done = False
if 'last_button' not in st.session_state:
    st.session_state.last_button = None


def button_click(value):
    """Handle button click events"""
    current = st.session_state.current_input

    # Reset after calculation if new number is entered
    if st.session_state.calculation_done and value not in ['+', '-', '×', '÷', '%', '.', '√', 'x²']:
        st.session_state.current_input = value
        st.session_state.calculation_done = False
        return

    # Keep result if operator is pressed after calculation
    elif st.session_state.calculation_done and value in ['+', '-', '×', '÷', '%', '.', '√', 'x²']:
        st.session_state.calculation_done = False

    # Handle clear button
    if value == 'C':
        st.session_state.current_input = '0'
        st.session_state.calculation_done = False
        return

    # Handle backspace
    elif value == '⌫':
        if len(current) > 1:
            st.session_state.current_input = current[:-1]
        else:
            st.session_state.current_input = '0'
        return

    # Handle square root
    elif value == '√':
        try:
            result = sqrt(float(current))
            st.session_state.current_input = str(result)
            st.session_state.calculation_done = True
        except:
            st.session_state.current_input = 'Error'
        return

    # Handle square
    elif value == 'x²':
        try:
            result = pow(float(current), 2)
            st.session_state.current_input = str(result)
            st.session_state.calculation_done = True
        except:
            st.session_state.current_input = 'Error'
        return

    # Handle equals
    elif value == '=':
        try:
            # Replace symbols for evaluation
            expr = current.replace('×', '*').replace('÷', '/')
            # Handle percentage calculations
            expr = re.sub(r'(\d+)%', r'(\1/100)', expr)
            result = str(eval(expr))
            st.session_state.current_input = result
            st.session_state.calculation_done = True
        except:
            st.session_state.current_input = 'Error'
        return

    # Handle decimal point
    elif value == '.':
        parts = re.split(r'\+|\-|\×|\÷|\%', current)
        if '.' not in parts[-1]:
            if current == '0' or st.session_state.last_button in ['+', '-', '×', '÷', '%']:
                st.session_state.current_input += '.'
            else:
                st.session_state.current_input += value
        return

    # Handle operators
    elif value in ['+', '-', '×', '÷', '%']:
        if st.session_state.last_button in ['+', '-', '×', '÷', '%']:
            st.session_state.current_input = current[:-1] + value
        else:
            st.session_state.current_input += value
        return

    # Handle numbers
    if current == '0':
        st.session_state.current_input = value
    else:
        st.session_state.current_input += value

    st.session_state.last_button = value


def handle_keypress():
    """Handle keyboard input"""
    if 'keyboard_input' in st.session_state:
        key = st.session_state.keyboard_input
        key_mapping = {
            '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
            '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
            '+': '+', '-': '-', '*': '×', '/': '÷', '%': '%',
            '.': '.', '=': '=', '\r': '=', '\n': '=',
            's': '√', 'S': '√', '^': 'x²',
            'Backspace': '⌫', 'Delete': '⌫',
            'Escape': 'C', 'c': 'C', 'C': 'C'
        }

        if key in key_mapping:
            button_click(key_mapping[key])
            # Clear the input after processing
            st.session_state.keyboard_input = ''


# Calculator UI
st.set_page_config(layout="centered")
st.title("🧮 Fixed Streamlit Calculator")
st.caption("Use mouse or keyboard (+, -, *, /, %, s for √, ^ for x²)")

# Display area
result_display = st.empty()
result_display.text_input("Result", st.session_state.current_input,
                          key="display", disabled=True,
                          label_visibility="collapsed")

# Create calculator buttons with proper symbols
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=button_click, args=('7',), key='7', use_container_width=True)
    st.button("4", on_click=button_click, args=('4',), key='4', use_container_width=True)
    st.button("1", on_click=button_click, args=('1',), key='1', use_container_width=True)
    st.button("C", on_click=button_click, args=('C',), key='C', use_container_width=True)

with col2:
    st.button("8", on_click=button_click, args=('8',), key='8', use_container_width=True)
    st.button("5", on_click=button_click, args=('5',), key='5', use_container_width=True)
    st.button("2", on_click=button_click, args=('2',), key='2', use_container_width=True)
    st.button("0", on_click=button_click, args=('0',), key='0', use_container_width=True)

with col3:
    st.button("9", on_click=button_click, args=('9',), key='9', use_container_width=True)
    st.button("6", on_click=button_click, args=('6',), key='6', use_container_width=True)
    st.button("3", on_click=button_click, args=('3',), key='3', use_container_width=True)
    st.button(".", on_click=button_click, args=('.',), key='.', use_container_width=True)

with col4:
    st.button("÷", on_click=button_click, args=('÷',), key='÷', use_container_width=True)
    st.button("×", on_click=button_click, args=('×',), key='×', use_container_width=True)
    st.button("-", on_click=button_click, args=('-',), key='.-', use_container_width=True)
    st.button("+", on_click=button_click, args=('+',), key='.+', use_container_width=True)

# Additional functions row
col5, col6, col7, col8 = st.columns(4)
with col5:
    st.button("√", on_click=button_click, args=('√',), key='√', use_container_width=True)
with col6:
    st.button("x²", on_click=button_click, args=('x²',), key='x²', use_container_width=True)
with col7:
    st.button("%", on_click=button_click, args=('%',), key='%', use_container_width=True)
with col8:
    st.button("⌫", on_click=button_click, args=('⌫',), key='⌫', use_container_width=True)

# Equals button
st.button("=", on_click=button_click, args=('=',), key='=', type="primary", use_container_width=True)

# Keyboard input - fixed implementation
st.text_input("Keyboard input (type here then press Enter)",
              key="keyboard_input",
              on_change=handle_keypress,
              label_visibility="collapsed")

# Continuous display update
result_display.text_input("", st.session_state.current_input,
                          key="display_update", disabled=True,
                          label_visibility="collapsed")