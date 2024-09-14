import csv
from collections import Counter
import re

def get_most_common_words(input_file, output_file, num_top_words=30):
    # Opening and reading the contents of the text file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Cleaning and normalizing the text (strip non-alphanumeric characters and convert to lowercase)
    content = re.sub(r'[^a-zA-Z\s]', '', content)
    words_list = content.lower().split()

    # Counting occurrences of each word
    word_frequency = Counter(words_list)

    # Retrieving the most frequent words
    most_common_words = word_frequency.most_common(num_top_words)

    # Writing the top words to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Word', 'Count'])  # Write header row

        for word, count in most_common_words:
            writer.writerow([word, count])


input_file = 'aggregated_texts.txt'
output_file = 'top_words.csv'
get_most_common_words(input_file, output_file)
