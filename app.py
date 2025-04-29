# streamlit_app.py
import streamlit as st
from lang_detection import test_language
import os

st.set_page_config(page_title="Language Detector", layout="centered")
st.title("🌍 Language Detection App")

# Text input
paragraph = st.text_area("Enter a paragraph to detect its language:")

# Button to trigger detection
if st.button("Detect Language"):
    if paragraph.strip() == "":
        st.warning("Please enter a paragraph before clicking the button.")
    else:
        # Save paragraph to a temporary file (since test_language expects a filepath)
        test_file_path = "test.txt"
        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write(paragraph)

        try:
            language = test_language(test_file_path)
            st.success(f"✅ Detected Language: **{language}**")
        except FileNotFoundError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
