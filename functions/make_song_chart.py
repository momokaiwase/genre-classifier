# Generates a csv file where each row contains: (Artist Name, Artist ID, Song Name, Song ID, Song Lyrics)
from time import sleep
from dotenv import load_dotenv
from lyricsgenius import Genius
from bs4 import BeautifulSoup
import requests
import pathlib
import csv
import os

# Stores all song chart data
song_chart = []

# Loads .env, which contains the client token
load_dotenv()

# Initializes the Genius API client token
client_token = os.getenv("CLIENT_TOKEN")

# Creates filepath for lyrics
file_path = os.path.abspath('.') + ('/')
pathlib.Path(file_path + 'lyrics/').mkdir(exist_ok=True) # Creates the lyrics directory if it does not currently exist

### Returns a list of the top 500 artist names
def get_names(file):
    # Stores artist names
    artist_names = []

    # Iterate througn the top 500 artists and store their names in artist_names
    with open(file, newline='', encoding='utf-8') as csvfile:
        # Initializes the CSV reader
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skips the first (header) row
        next(csvreader)

        for row in csvreader:
            # print(row)
            artist_names.append(row[1])

    return artist_names

# print(get_names('top_500_spotify_artists.csv'))

### Given an artist name from artist_names, searches it in the Genius API and returns its (Artist Name, Artist ID, Song Name, Song ID, Lyrics)
def get_artist_data(name):
    # Stores all the tracks from the same artist
    artist_data = []
    
    # Initialize Genius search
    genius = Genius(client_token)

    # Searches for Artist object associated with name
    artist = genius.search_artist(name, max_songs=20)

    # Loops through each song in the artist's catalogue
    for i in range(len(artist.songs)):
        row = (name, artist.id, artist.songs[i].title, artist.songs[i].id, artist.songs[i].lyrics)
        artist_data.append(row)

    return artist_data   

names = get_names("top_500_spotify_artists.csv")

for name in names:
    song_chart.extend(get_artist_data(name))

# Save data to a CSV file
with open('song_chart.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Artist Name', 'Artist ID', 'Song Title', 'Song ID', 'Song Lyrics'])
    writer.writerows(song_chart)

print('song_chart.csv saved successfully!')