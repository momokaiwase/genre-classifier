import pandas as pd

# Define your desired column names
column_names = ['Artist', 'random', 'Song Title', 'random2', 'Lyrics']

# Read the CSV assuming it has no header
df = pd.read_csv('songs420.csv', header=None, names=column_names)

# Save it back with the new header
df.to_csv('songs420_header.csv', index=False)