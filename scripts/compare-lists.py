import pandas as pd
import os
from collections import Counter

# Define the paths for the input and output folders
input_folder = 'input'
output_folder = 'output'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to determine delimiter
def determine_delimiter(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()
        if ';' in first_line:
            return ';'
        return ','

# List all CSV files in the input directory
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

if len(csv_files) < 2:
    raise ValueError('Need at least two CSV files in the input directory.')

# Determine delimiters
delimiter_file1 = determine_delimiter(os.path.join(input_folder, csv_files[0]))
delimiter_file2 = determine_delimiter(os.path.join(input_folder, csv_files[1]))

# Load the CSV files into DataFrames with the determined delimiters
df1 = pd.read_csv(os.path.join(input_folder, csv_files[0]), delimiter=delimiter_file1)
df2 = pd.read_csv(os.path.join(input_folder, csv_files[1]), delimiter=delimiter_file2)

# Print column names to debug
print("Columns in first file:", df1.columns.tolist())
print("Columns in second file:", df2.columns.tolist())

# Define column names for each file
column_name_file1 = 'DestAddress'
column_name_file2 = 'owner'

# Strip whitespace from column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Count occurrences of each address in both files
count1 = Counter(df1[column_name_file1].dropna())
count2 = Counter(df2[column_name_file2].dropna())

# Find missing addresses with counts
missing_in_df1 = [(address, count2[address] - count1.get(address, 0)) for address in count2 if count2[address] > count1.get(address, 0)]
missing_in_df2 = [(address, count1[address] - count2.get(address, 0)) for address in count1 if count1[address] > count2.get(address, 0)]

# Create output files
output_file1 = os.path.join(output_folder, 'missing_in_file1.txt')
output_file2 = os.path.join(output_folder, 'missing_in_file2.txt')

# Write missing addresses to files
with open(output_file1, 'w') as f:
    f.write(f'Missing in {csv_files[1]}: {sum(count for address, count in missing_in_df2)}\n')
    for address, count in missing_in_df2:
        for _ in range(count):
            f.write(f'{address}\n')

with open(output_file2, 'w') as f:
    f.write(f'Missing in {csv_files[0]}: {sum(count for address, count in missing_in_df1)}\n')
    for address, count in missing_in_df1:
        for _ in range(count):
            f.write(f'{address}\n')

print(f'Results have been written to {output_folder}.')
