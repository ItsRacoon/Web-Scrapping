import pandas as pd

# Load your dataset
df = pd.read_csv('Scrapped_Data.csv')

# Display the first few rows to understand the structure of the data
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Handle missing values
# For example, you can drop rows with missing values
df.dropna(inplace=True)

# Or fill missing values with a specific value
# df.fillna(value, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert data types if necessary
# For example, converting a column to datetime
# df['date_column'] = pd.to_datetime(df['date_column'])

# Standardize text data
# For example, converting text to lowercase
# df['text_column'] = df['text_column'].str.lower()

# Remove outliers
# For example, you can remove rows where a numeric column exceeds a certain threshold
# df = df[df['numeric_column'] < threshold]

# Perform other necessary cleaning operations based on your dataset

# Save the cleaned dataset
df.to_csv('cleaned_dataset.csv')
