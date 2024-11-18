import streamlit as st
import streamlit.components.v1 as components

# Enable wide layout
st.set_page_config(layout="wide")

# Title for the Streamlit app
st.title("Interactive Periodic Table App with OpenAI ChatGPT")

# Embed the HTML file with auto-scaling height
with open("periodic_table.html", "r") as f:
    html_code = f.read()

# Dynamically scale the height based on screen size
components.html(html_code, height=1500, width=1920, scrolling=True)
