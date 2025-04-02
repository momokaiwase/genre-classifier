### Contains helper functions for making song chart rows.
from dotenv import load_dotenv
from lyricsgenius import Genius
import csv
import os

# Stores all song chart data
song_chart = []

# Loads .env, which contains the client token
load_dotenv()

# Initializes the Genius API client token
client_token = os.getenv("CLIENT_TOKEN")

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
        row = (name, artist.id, artist.songs[i].title, artist.songs[i].id, artist.songs[i].lyrics.replace('\n',' '))
        artist_data.append(row)

    return artist_data   
