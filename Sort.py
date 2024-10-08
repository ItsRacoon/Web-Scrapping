import pandas as pd

# Read in your .csv files as dataframes
# df is a common standard for naming a dataframe. You can
# name them something more descriptive as well.
# Using a descriptive name is helpful when you are dealing
# with multiple .csv files.
df = pd.read_csv("Scrapped_Data.csv")

# the .sort_values method returns a new dataframe, so make sure to
# assign this to a new variable.
sorted_df = df.sort_values(by=["Price"], ascending=False)

# Index=False is a flag that tells pandas not to write
# the index of each row to a new column. If you'd like
# your rows to be numbered explicitly, leave this as
# the default, True
sorted_df.to_csv('homes_sorted.csv', index=False)