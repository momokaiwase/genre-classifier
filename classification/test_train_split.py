import csv
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import os

##SPLIT TRAINING AND TESTING DATA
#make separate csv files for split testing and training data for BERT and LLM classification

#check working directory (where files will be saved): 
# print("Current working directory:", os.getcwd())

# Load CSV as DataFrame
df = pd.read_csv('raw_lyrics_genrelabel_int.csv', on_bad_lines='skip', delimiter='\t')

#split training and test data
train_df, test_df = train_test_split(df[['Lyrics', 'Genre_Label']], test_size=0.2, random_state=42)
print("Train data shape:", train_df.shape)
print("Test data shape:", test_df.shape)

# Save to CSV with headers
train_df.to_csv('raw_lyrics_train_dataset.csv', index=False)
test_df.to_csv('raw_lyrics_test_dataset.csv', index=False)