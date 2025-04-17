### Contains helper functions for making, navigating, and reading song chart rows.
from dotenv import load_dotenv
from lyricsgenius import Genius
import csv
import os

# Global variable for storing max song search per artist. --MODIFY THIS VARIABLE TO ALTER NUMBER OF SONGS PER ARTIST--
MAX_SONGS = 15

# Stores all song chart data
song_chart = []

# Loads .env, which contains the client token
load_dotenv()

# Initializes the Genius API client token
client_token = os.getenv("CLIENT_TOKEN")

### Returns a list of the top artist names
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
    # This loop keeps retrying the search whenever a timeout occurs

    # Tracks the amount of times a search has reset
    reset_count = 0
    while True:
        if reset_count == 10:
            return False

        try:
            artist = genius.search_artist(name, max_songs=MAX_SONGS)
            break
        except:
            reset_count += 1
            pass

    #resolves artist NoneType error
    if artist is None:
        return False
    
    # Loops through each song in the artist's catalogue
    for i in range(len(artist.songs)):
        row = (name, artist.id, artist.songs[i].title, artist.songs[i].id, artist.songs[i].lyrics.replace('\n',' '))
        artist_data.append(row)

    return artist_data

### Given a song and artist name, searches it in the Genius API and returns its (Artist Name, Artist ID, Song Name, Song ID, Lyrics)
def get_song_data(song):
    # Initialize Genius search
    genius = Genius(client_token)

    # Stores song data
    song_data = []

    # Searches for Song object associated with name
    # This loop keeps retrying the search whenever a timeout occurs

    # Tracks the amount of times a search has reset
    reset_count = 0
    while True:
        if reset_count == 10:
            return False

        try:
            data = genius.search_song(song)
            artist_id = genius.search_artist(data.artist, max_songs=0).id
            break
        except:
            reset_count += 1
            pass
    
    if song is None:
        return False
    
    # Formats and returns row
    row = (data.artist, artist_id, song, data.id, data.lyrics.replace('\n', ' '))
    song_data.append(row)

    return song_data

# print(get_song_data('Not Like Us'))

### Given a list of artist names, returns a list of all song titles attributed to those artists.
def get_artist_titles(names):
    # Stores song titles
    res = []

    with open('song_chart.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Initialize the CSV reader
        csvreader = csv.reader(csvfile)

        # For each row, if the artist is in the names parameter, add the song name to the result
        for row in csvreader:
            if row[0] in names:
                res.append(row[2])
    
    return res

### Gets all songs titles recorded in top_spotify_songs.csv
def get_all_songs():
    # Stores song titles
    res = []

    with open('top_spotify_songs.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Init CSV reader
        csvreader = csv.reader(csvfile)
        header = next(csvreader)

        for row in csvreader:
            res.append(row[2])

    return res