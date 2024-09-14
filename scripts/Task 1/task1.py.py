import pandas as pd

# Define a list of CSV filenames and their respective text column names
Given_csv = [('CSV1.csv', 'SHORT-TEXT'), ('CSV2.csv', 'TEXT'), ('CSV3.csv', 'TEXT'), ('CSV4.csv', 'TEXT')]

# Create a list to collect text data from all CSV files
combined_texts = []

# Process each CSV file and extract text data
for filename, column_name in Given_csv:
    # Load the CSV file into a DataFrame
    dataframe = pd.read_csv(filename)

    # Check if the specified column exists in the DataFrame
    if column_name in dataframe.columns:
        # Convert the text column to a list of strings and append to the combined list
        combined_texts.extend(dataframe[column_name].astype(str).tolist())

# Save the aggregated text data to a new text file
output_filename = 'aggregated_texts.txt'
with open(output_filename, 'w', encoding='utf-8') as file:
    for text in combined_texts:
        file.write(text + '\n')

print(f'The text data has been successfully written to {output_filename}')
