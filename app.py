from flask import Flask, render_template, request, jsonify
from lang_detection import test_language
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/detect_language', methods=['POST'])
# Task 10: Handle and Route the Request Object - Define the detect_language() function
def detect_language():
    paragraph = request.form['paragraph']
    # Store paragraph in a file named test.txt in the flaskapplication directory
    with open('test.txt', 'w') as file:
        file.write(paragraph)
    language = test_language('test.txt')
    return render_template('result.html', language=language)

if __name__ == "__main__":
    app.run(debug=True)