import os
import pandas as pd

# Function to process a single CSV file and extract rows where a particular column contains the keyword "TEXT"
def process_csv_for_text(file_path, keyword="TEXT"):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Initialize a list to hold the extracted text data
    extracted_data = []
    
    # Loop through the DataFrame to find rows where any column contains the keyword "TEXT"
    for index, row in df.iterrows():
        # Check if any cell in the row contains the keyword "TEXT" (case-insensitive)
        if row.astype(str).str.contains(keyword, case=False).any():
            # Extract the actual values from the row without column names or index
            row_data = " | ".join([str(value) for value in row.values])  # Convert only the row's values
            # Append this row data to the extracted_data list
            extracted_data.append(row_data)
    
    return extracted_data

# Main function to process all CSV files in a folder and collect data from rows that contain the keyword "TEXT"
def process_all_csv_files_for_text(folder_path, output_txt_file, keyword="TEXT", limit=30):
    # Initialize a list to hold all extracted text data across all CSV files
    all_extracted_data = []
    
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV file
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            # Extract rows containing the keyword "TEXT" from the current CSV file
            extracted_data = process_csv_for_text(file_path, keyword)
            # Append the extracted data to the overall list
            all_extracted_data.extend(extracted_data)
    
    # Limit the extracted data to the top 'limit' entries
    top_extracted_data = all_extracted_data[:limit]
    
    # Save the top extracted data to the output text file
    with open(output_txt_file, 'w') as f:
        for line in top_extracted_data:
            f.write(line + "\n")

    print(f"Top {limit} extracted data saved to {output_txt_file}")

# Specify the folder containing the CSV files and the output file
input_folder = "csv"
output_txt_file = "output_data.txt"

# Call the function to process all CSV files and extract rows containing the keyword "TEXT"
process_all_csv_files_for_text(input_folder, output_txt_file, keyword="TEXT", limit=30)
