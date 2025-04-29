# Multilingual Language Detection using n-Grams

This project is a **Language Detection System** built using Python and Flask. It detects the language of a given paragraph of text by analyzing character-level **n-gram frequency patterns** across multiple languages.

## 🌍 Supported Languages

- English (eng)
- French (fra)
- German (deu)
- Spanish (spa)
- Chinese (zho)
- Japanese (jpn)
- Hindi (hin) ✅

## 🔍 How It Works

1. **Data Collection**: Automatically downloads public domain books from [Project Gutenberg](https://www.gutenberg.org/).
2. **Preprocessing**:
   - Removes boilerplate text
   - Cleans and tokenizes text
   - Generates character-level n-grams (1 to 5)
3. **Training**: Computes frequency-based language models for each language.
4. **Testing**: Takes a user input, generates its n-grams, and compares with trained frequency tables using out-of-order metric.
5. **Web App**: Simple Flask UI to input paragraph and detect its language.

## 🛠 Tech Stack

- Python
- Flask
- Regular Expressions (`regex`)
- `pycountry`, `requests`, `collections`
- HTML (Jinja templates)

## 📁 Project Structure

Language_Detector├── dataset/ # Raw book text files ├── tokenized/ # Tokenized versions ├── nGrams/ # n-gram models per language ├── processed/ # n-gram frequency files ├── test.txt # Temporary input file ├── templates/ │ ├── index.html │ └── result.html ├── app.py # Flask app └── lang_detection.py # Core logic


## ▶️ How to Run

1. Clone this repo:
   ```bash
   git clone [https://github.com/yourusername/lang-detection-ngram.git](https://github.com/abhi7275/Language-Detector.git)
   cd Language-Detector
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app : python app.py

🧠 What I Learned
Character-level text preprocessing

Efficient n-gram generation

Rank-based language detection

Handling multilingual datasets

Integrating backend logic with Flask frontend

🚀 Future Improvements
Add support for more Indian languages

Integrate with Hugging Face or Wikipedia Hindi dumps

Deploy online with Docker or Streamlit

Switch to ML-based classification (e.g., Naive Bayes)
