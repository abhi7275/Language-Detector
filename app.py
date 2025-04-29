# streamlit_app.py
import streamlit as st
from lang_detection import test_language

st.title("Language Detection App")

# Text input
paragraph = st.text_area("Enter your paragraph below:")

# Button to trigger detection
if st.button("Detect Language"):
    # Save to a file (if your function depends on reading from a file)
    with open("test.txt", "w") as f:
        f.write(paragraph)

    # Call language detection logic
    language = test_language("test.txt")

    # Show result
    st.success(f"Detected Language: {language}")
