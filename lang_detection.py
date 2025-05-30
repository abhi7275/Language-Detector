# Task 1: Import Libraries
import os
import requests
import pycountry
import regex
import collections

# Task 2: Get the Data --- Create get_books_text() function
def get_books_text(output_directory='/Language-Detector/', language_code="eng"):
    language_codes = language_codes = ['fra', 'deu', 'eng', 'spa', 'zho', 'jpn', 'hin']
    urls = [
        [
            # French books
            "https://www.gutenberg.org/cache/epub/51709/pg51709.txt",
            "https://www.gutenberg.org/cache/epub/18092/pg18092.txt",
            "https://www.gutenberg.org/cache/epub/13704/pg13704.txt",
            "https://www.gutenberg.org/cache/epub/16901/pg16901.txt",
            "https://www.gutenberg.org/cache/epub/44715/pg44715.txt",
            "https://www.gutenberg.org/cache/epub/11049/pg11049.txt",
            "https://www.gutenberg.org/cache/epub/14536/pg14536.txt",
            "https://www.gutenberg.org/cache/epub/51826/pg51826.txt",
            "https://www.gutenberg.org/cache/epub/50435/pg50435.txt",
            "https://www.gutenberg.org/cache/epub/28523/pg28523.txt"
        ],
        [
            # Hindi books
            "https://www.gutenberg.org/cache/epub/37796/pg37796.txt",
            
        ],

        [
            # German books
            "https://www.gutenberg.org/cache/epub/15787/pg15787.txt",
            "https://www.gutenberg.org/cache/epub/16264/pg16264.txt",
            "https://www.gutenberg.org/cache/epub/19755/pg19755.txt",
            "https://www.gutenberg.org/cache/epub/14075/pg14075.txt",
            "https://www.gutenberg.org/cache/epub/22492/pg22492.txt",
            "https://www.gutenberg.org/cache/epub/17379/pg17379.txt",
            "https://www.gutenberg.org/cache/epub/19460/pg19460.txt",
            "https://www.gutenberg.org/cache/epub/20613/pg20613.txt",
            "https://www.gutenberg.org/cache/epub/6343/pg6343.txt",
            "https://www.gutenberg.org/cache/epub/6342/pg6342.txt"
        ],
        [
            # English books
            "https://www.gutenberg.org/cache/epub/20724/pg20724.txt",
            "https://www.gutenberg.org/cache/epub/19238/pg19238.txt",
            "https://www.gutenberg.org/cache/epub/19291/pg19291.txt",
            "https://www.gutenberg.org/cache/epub/19285/pg19285.txt",
            "https://www.gutenberg.org/cache/epub/19296/pg19296.txt",
            "https://www.gutenberg.org/cache/epub/19300/pg19300.txt",
            "https://www.gutenberg.org/cache/epub/48916/pg48916.txt",
            "https://www.gutenberg.org/cache/epub/22600/pg22600.txt",
            "https://www.gutenberg.org/cache/epub/29107/pg29107.txt",
            "https://www.gutenberg.org/cache/epub/21993/pg21993.txt"
        ],
        [
            # Spanish books
            "https://www.gutenberg.org/cache/epub/33461/pg33461.txt",
            "https://www.gutenberg.org/cache/epub/36986/pg36986.txt",
            "https://www.gutenberg.org/cache/epub/16109/pg16109.txt",
            "https://www.gutenberg.org/cache/epub/20099/pg20099.txt",
            "https://www.gutenberg.org/cache/epub/46201/pg46201.txt",
            "https://www.gutenberg.org/cache/epub/68443/pg68443.txt",
            "https://www.gutenberg.org/cache/epub/13608/pg13608.txt",
            "https://www.gutenberg.org/cache/epub/43017/pg43017.txt",
            "https://www.gutenberg.org/cache/epub/55038/pg55038.txt",
            "https://www.gutenberg.org/cache/epub/63509/pg63509.txt",
        ],
        [
            # Chinese books
            "https://www.gutenberg.org/cache/epub/24225/pg24225.txt",
            "https://www.gutenberg.org/cache/epub/25328/pg25328.txt",
            "https://www.gutenberg.org/cache/epub/27119/pg27119.txt",
            "https://www.gutenberg.org/cache/epub/24185/pg24185.txt",
            "https://www.gutenberg.org/cache/epub/24051/pg24051.txt",
            "https://www.gutenberg.org/cache/epub/23841/pg23841.txt",
            "https://www.gutenberg.org/cache/epub/24041/pg24041.txt",
            "https://www.gutenberg.org/cache/epub/27329/pg27329.txt",
            "https://www.gutenberg.org/cache/epub/24058/pg24058.txt",
            "https://www.gutenberg.org/cache/epub/23948/pg23948.txt"
        ],
        [
            # Japanese books
            "https://www.gutenberg.org/cache/epub/1982/pg1982.txt",
            "https://www.gutenberg.org/cache/epub/34013/pg34013.txt",
            "https://www.gutenberg.org/cache/epub/39287/pg39287.txt",
            "https://www.gutenberg.org/cache/epub/35018/pg35018.txt",
            "https://www.gutenberg.org/cache/epub/34013/pg34013.txt",
            "https://www.gutenberg.org/cache/epub/34158/pg34158.txt",
            "https://www.gutenberg.org/cache/epub/41325/pg41325.txt",
            "https://www.gutenberg.org/cache/epub/36358/pg36358.txt",
            "https://www.gutenberg.org/cache/epub/35018/pg35018.txt",
            "https://www.gutenberg.org/cache/epub/32978/pg32978.txt"
        ],
    ]


    # Traverse the elements of the combined list
    for index, url_list in enumerate(urls, start=0):

        language = (pycountry.languages.get(alpha_3=language_codes[index])).name
        print("Getting data for " ,language)
        books_text = []
        cleaned_text = ""
        tokens = []

        for sublist in enumerate(url_list, start=0):
            # Sublist is a tuple
            url= sublist[1]
            try:
                # Download the book text
                response = requests.get(url)
                response.raise_for_status()  # Check for errors

                # Decode the content assuming it's UTF-8
                raw_text = response.content.decode('utf-8', errors='ignore').strip()


                # -----------Preprocessing functions-------- #
                # Skip the table of contents and introductory material
                cleaned_text = cleaned_text + skip_template_text(raw_text)
                # Make tokens of the text
                tokens.append( split_and_pad (cleaned_text) )

                books_text.append(raw_text)
            except requests.exceptions.RequestException as e:
                print(f"Error downloading book from {url}: {e}")
                # Continue to the next book if there is an error

        # Store the raw text in a file
        filename = os.path.join(output_directory, "dataset", f"{language}.txt")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(books_text[0])
        filename_int1 = os.path.join(output_directory, "tokenized", f"{language}.int1.txt")
        with open(filename_int1, 'w', encoding='utf-8') as file:
            for item in tokens[0]:
                file.write(item)
    return

# Task 3: Preprocess the Data --- Implement functions
def split_and_pad(text):
    tokens = regex.findall(r"\b\p{L}+\'*\p{L}*\b", text, flags=regex.UNICODE)
    padded_tokens = [token.lower() + '\n' for token in tokens]
    return padded_tokens

def data_cleaning(raw_text):
    regex_pattern = r"[，!\"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~\\0-9]"

    # Use the sub() method to replace matches with an empty string
    return regex.sub(regex_pattern, "", raw_text)

def skip_template_text(text):
    start_phrase = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_phrase_1 = "*** END OF THE PROJECT GUTENBERG EBOOK"
    end_phrase_2 = "End of Project Gutenbergs"
    pattern = regex.compile(f'{regex.escape(start_phrase)}(.*?){regex.escape(end_phrase_1)}|{regex.escape(end_phrase_2)}', regex.DOTALL)
    match = pattern.search(text)
    if match:
        start_idx = match.start() + len(start_phrase)
        end_idx = match.end() - 50
        intermediate_stage = text[start_idx:end_idx]
        index = intermediate_stage.find("***")
        if index != -1:
            text = intermediate_stage[index + 600 + len("***"):].strip()
    return data_cleaning(text)
# Task 4: Generate nGrams
def generate_ngrams(line):
    ngrams = []
    n = len(line)
    for i in range(n):
        for j in range(1, min(n - i, 6)):
            ngrams.append(line[i:i+j])
    return ngrams

# Task 5:Count and Sort nGrams by Frequency
def count_ngram_frequency(ngrams):
    return collections.Counter(ngrams)
def sort_ngrams_by_frequency(ngram_counter):
    return sorted(ngram_counter.items(), key=lambda x: (-x[1], x[0]))
# Task 6: Call nGrams Functions --- Implement the generate_and_count_ngrams() function
def generate_and_count_ngrams(input_file_path, output_file_path, frequency_file_path):
    n_gram_counts = collections.Counter()

    with open(input_file_path, 'r', encoding='UTF-8') as input_file:
        for line in input_file:
            line = line.strip()
            ngrams = generate_ngrams(line)
            n_gram_counts += count_ngram_frequency(ngrams)

    sorted_ngrams = sort_ngrams_by_frequency(n_gram_counts)

    with open(output_file_path, 'w', encoding='UTF-8') as output_file, \
        open(frequency_file_path, 'w', encoding='UTF-8') as frequency_file:

        for n_gram, count in sorted_ngrams:
            output_file.write(f"{n_gram}\n")
            frequency_file.write(f"{n_gram}: {count}\n")

# Task 7: Preprocess the Test File
def preprocess_file(file_name):
    tokenized_lines = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.strip().replace(' ', '_ _')
            tokenized_lines.append(f'_{line}_\n')
    return tokenized_lines

# Task 8: Test the Model --- Implement the function
def test_language(file_name):
    directory =os.path.join(os.path.dirname(__file__), "nGrams")
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist. Please ensure it is created and populated with the necessary files.")

    trained_languages = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.nGrams.txt')]
    print(trained_languages)
    tokenized_lines = preprocess_file(file_name)
    n_gram_counts = collections.Counter()
    for line in tokenized_lines:
        ngrams = generate_ngrams(line)
        n_gram_counts += count_ngram_frequency(ngrams)

    sorted_ngrams = sort_ngrams_by_frequency(n_gram_counts)
    out_of_order = []
    for language_file in trained_languages:
        with open(language_file, 'r', encoding='UTF-8') as file:
            train_ngrams = [line.strip() for line in file]
        rank_table = {ngram: rank for rank, ngram in enumerate(train_ngrams, start=1)}
        out_of_order.append(sum(abs(rank_table.get(ngram, 50000) - rank) for rank, (ngram, _) in enumerate(sorted_ngrams, start=1)))

    min_index = out_of_order.index(min(out_of_order))
    identified_language = trained_languages[min_index]
    result = os.path.basename(identified_language)[:-10]
    return result


if __name__ == "__main__":
    # Task 2: Get the Data --- Function Call
    # Get text of books and store in files in processed form
    get_books_text()

    # Task 6: Call n-grams Functions --- Function Call
    # Generate and count n-grams of all the languages
    language_codes = ['fra', 'deu', 'eng', 'spa', 'zho', 'jpn']
    for item in language_codes:
        language = (pycountry.languages.get(alpha_3=item)).name
        input_file_path = f"/Language-Detector/tokenized/{language}.int1.txt"
        n_gram_file_path = f"/Language-Detector/nGrams/{language}.nGrams.txt"
        frequency_file_path = f"/Language-Detector/processed/{language}.nGramsFrequency.txt"
        print("Processing ", language, " for nGrams!")
        generate_and_count_ngrams(input_file_path, n_gram_file_path, frequency_file_path)   

    # Task 8: Test the Model --- Function Call
    file_name = "/Language-Detector/test.txt"
    lang_result = test_language(file_name)
    print(f"Identified Language = {lang_result}")
