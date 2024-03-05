import streamlit as st
import requests

st.title('Research Paper Summarization Engine')

API_URL = "http://127.0.0.1:8000/summarize"

user_review = st.text_area("Write the research paper abstract here:")

if st.button('Summarize'):
    if user_review:
        response = requests.post(API_URL, json={"review": user_review})
        if response.status_code == 200:
            data = response.json()
            result = data["result"]
            confidence = data["confidence"]
            st.write(f"Predicted Sentiment: {result} (Confidence: {confidence:.2f})")
        else:
            st.write("Failed to get a response from the model.")
    else:
        st.write("Please enter a review for prediction.")
