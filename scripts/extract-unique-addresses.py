import pandas as pd
import os

# Define the paths for the input and output folders
input_folder = 'input'
output_folder = 'output'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all CSV files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.csv'):
        # Construct the full path for the input file
        file_path = os.path.join(input_folder, file_name)

        try:
            # Load the CSV file with the correct delimiter
            df = pd.read_csv(file_path, delimiter=';')

            # Select only the 'owner' column, remove duplicates
            unique_addresses = df['owner'].drop_duplicates()

            # Convert the Series to a DataFrame and rename the column
            unique_addresses_df = unique_addresses.reset_index(drop=True).to_frame(name='wallet')

            # Construct the full path for the output file
            output_file_name = f'unique_addresses_{os.path.splitext(file_name)[0]}.csv'
            output_file_path = os.path.join(output_folder, output_file_name)

            # Save the DataFrame to a new CSV file with a header
            unique_addresses_df.to_csv(output_file_path, index=False)

            print(f"Unique addresses from {file_name} have been saved to {output_file_path}")

        except Exception as e:
            print(f"An error occurred while processing {file_name}: {e}")
