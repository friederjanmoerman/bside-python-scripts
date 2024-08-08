import pandas as pd
import os

# Define the paths for the input and output folders
input_folder = 'input'
output_folder = 'output'

# Construct the full path for the input file
input_file_name = 'path_to_your_file.csv'
file_path = os.path.join(input_folder, input_file_name)

# Load the CSV file with the correct delimiter
df = pd.read_csv(file_path, delimiter=';')

# Select only the 'owner' column, remove duplicates
unique_addresses = df['owner'].drop_duplicates()

# Construct the full path for the output file
output_file_name = 'unique_addresses.csv'
output_file_path = os.path.join(output_folder, output_file_name)

# Save the unique addresses to a new CSV file
unique_addresses.to_csv(output_file_path, index=False, header=False)

print(f"Unique addresses have been saved to {output_file_path}")
