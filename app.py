
import os
import sys
import streamlit as st

sys.path.insert(0, './dashboard')


st.set_page_config(page_title="Sales    ", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Pharmaceutical-Sales-Prediction
""")

# Add all your application here


# The main app
app.run()
