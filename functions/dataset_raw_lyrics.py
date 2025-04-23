import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
bottom_half = pd.read_csv("tiffanysongs422.csv")
top_half = pd.read_csv("ricardosongs422.csv")
df_combined = pd.concat([top_half, bottom_half], ignore_index=True)
songs422 = pd.read_csv("songs422.csv")
songs422_labeled = pd.merge(songs422, df_combined[['Artist', 'Song Title', 'Genre']], on=['Artist', 'Song Title'], how='left')
missing_genre_count = songs422_labeled['Genre'].isnull().sum()
print(missing_genre_count)
songs422_labeled = songs422_labeled.dropna()

#songs422_labeled.to_csv('raw_lyrics.csv', index=False)
raw_lyrics = pd.read_csv("raw_lyrics.csv")
songs_420_header = pd.read_csv("songs420_header.csv")
lyrics_labeled = pd.merge(raw_lyrics[['Artist', 'Song Title', 'Genre']], songs_420_header[['Artist', 'Song Title', 'Lyrics']], on=['Artist', 'Song Title'], how='left')
lyrics_labeled.to_csv("raw_lyrics_genrelabel.csv", index=False)
