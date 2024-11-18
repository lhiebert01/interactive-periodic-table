import streamlit as st
import streamlit.components.v1 as components

# Enable wide layout
st.set_page_config(layout="wide")

# Title for the Streamlit app
st.title("Interactive Periodic Table App with OpenAI ChatGPT")

# Embed the HTML file with full-screen dimensions
with open("periodic_table.html", "r") as f:
    html_code = f.read()

components.html(html_code, height=1000, width=1920, scrolling=False)
