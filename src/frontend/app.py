# Import Libraries
import requests
import streamlit as st

# Initialization
API_URL = 'http://127.0.0.1:8000/summarize'

# Main UI
st.title("Research Paper Summarization Engine")
user_input = st.text_area("Write the research paper abstract here:")

# Summarize Button
if st.button("Summarize"):
    if user_input:
        response = requests.post(API_URL, json={"text": user_input})
        if response.status_code == 200:
            data = response.json()
            summary = data["summary"]
            st.write(f"Summary: {summary}")
        else:
            st.write("Failed to get a response from the model.")
    else:
        st.write("Please enter a research paper abstract to summarize.")