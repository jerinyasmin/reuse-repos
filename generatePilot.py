import pandas as pd

# Read the CSV file
file_path = ''   # the csv file location 
df = pd.read_csv(file_path)

# Randomly sample a specified number of rows from the DataFrame
sampled_df = df.sample(n=105, random_state=42)  # random_state is for reproducibility

# Save the sampled DataFrame to a new CSV file
sampled_output_file_path = '' # the csv file location 
sampled_df.to_csv(sampled_output_file_path, index=False)
