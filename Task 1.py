import os
import pandas as pd

# Function to process a single CSV file and extract rows where any cell contains the keyword
def process_csv_for_text(file_path, keyword="TEXT"):
    # Read the CSV file into a pandas DataFrame, with error handling for encoding
    try:
        df = pd.read_csv(file_path, encoding='utf-8', na_filter=False)  # Ensuring no NaN is treated as missing
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='ISO-8859-1', na_filter=False)  # Fallback to different encoding if needed
    
    # Convert the entire DataFrame to strings for comparison, handling non-string data
    df = df.applymap(str)
    
    # Check if any cell in each row contains the keyword (case-insensitive)
    mask = df.apply(lambda row: row.str.contains(keyword, case=False).any(), axis=1)
    
    # Extract rows that match the keyword and join their values with '|' for output
    extracted_data = df[mask].apply(lambda row: " | ".join(row.values), axis=1).tolist()
    
    return extracted_data

# Main function to process all CSV files in a folder and collect data from rows that contain the keyword
def process_all_csv_files_for_text(folder_path, output_txt_file, keyword="TEXT", limit=30):
    # Initialize a list to hold all extracted text data across all CSV files
    all_extracted_data = []
    
    # Counter for files processed and rows extracted
    files_processed = 0
    rows_extracted = 0
    
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV file
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            # Process the current CSV file and extract relevant rows
            extracted_data = process_csv_for_text(file_path, keyword)
            
            # Append the extracted data to the overall list
            all_extracted_data.extend(extracted_data)
            files_processed += 1
            rows_extracted += len(extracted_data)
    
    # Limit the extracted data to the top 'limit' entries
    top_extracted_data = all_extracted_data[:limit]
    
    # Save the top extracted data to the output text file, with error handling for file I/O
    with open(output_txt_file, 'w', encoding='utf-8') as f:
        for line in top_extracted_data:
            f.write(line + "\n")
    
    # Log the results
    print(f"Processed {files_processed} CSV file(s), extracted {rows_extracted} rows.")
    print(f"Top {limit} extracted data saved to {output_txt_file}")

# Specify the folder containing the CSV files and the output file
input_folder = "csv"
output_txt_file = "output_data.txt"

# Call the function to process all CSV files and extract rows containing the keyword
process_all_csv_files_for_text(input_folder, output_txt_file, keyword="TEXT", limit=30)
