import streamlit as st
import streamlit.components.v1 as components

# Title for the Streamlit app
st.title("Interactive Periodic Table App with OpenAI ChatGPT")

# Embed the HTML file
with open("periodic_table.html", "r") as f:
    html_code = f.read()

# Render the HTML content in Streamlit
components.html(html_code, height=800, scrolling=True)

# Add a footer or additional functionality if needed
st.write("This app allows educators, students, and enthusiasts to explore the periodic table and interact with OpenAI ChatGPT.")
