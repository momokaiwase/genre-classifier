### Sorts songs by genre tag various text documents.
from lyricsgenius import Genius
import chart_helper as ch
import requests
import json
import os

db_token = os.getenv("DB_TOKEN")
print(db_token)

### Given an artist and song, sorts it into respective text files in the genres/ directory
def genre_sort(artist, song):
    artist_format = artist.replace(' ', '_').lower()
    song_format = song.replace(' ', '_').lower()

    # Debug
    # print(f"***Artist: {artist}***")
    # print(f"***Song: {song}***")

    # TheAudioDB API test key
    key = db_token

    # Searches TheAudioDB for track details from artist & track name
    r = requests.get(f'https://www.theaudiodb.com/api/v1/json/{key}/searchtrack.php?s={artist_format}&t={song_format}')
    # r = requests.get(f'https://www.theaudiodb.com/api/v1/json/{key}/searchtrack.php?s=Kendrick_Lamar&t=Not_Like_Us')


    # Stores JSON result from API request
    result = r.text
    # print(result)

    # Converts JSON result to a Python dictionary
    info = json.loads(result)

    # Stores the genre of the track from the dictionary
    try:
        genre = info['track'][0]['strGenre']

        # Appends the track name to the respective genre text file
        with open(f'genres/{genre}.txt', 'a+', encoding='utf-8') as f:
            # Store all songs in the text file currently in a list
            f.seek(0, 0)
            sorted_songs = f.readlines()

            # If the current song is not already sorted, append it to the file
            if song + '\n' in sorted_songs:
                print(f'---{song} has already been recorded.---')

            else:
                f.write(song + '\n')
                print(f'---{song} successfully sorted in {genre}.txt!---')

    # TODO: Replace punctuation is song titles; that's probably what's causing this
    except:
        with open('genres/failed.txt', 'a+', encoding='utf-8') as f:
            f.write(song + '\n')
        print(f'---Search for {song} failed.---')

### Opens and iterates through song_chart.csv, running genre_sort() on each pair of artist and tracks
# Gets all names in song_chart.csv
names = ch.get_names('top_spotify_artists.csv')

# print(names)

# Iterates through the names, gets their songs, then sorts them into the respective genres
for name in names:
    for song in ch.get_titles(name):
        genre_sort(name, song)
    print(f'***{name}\'s songs have been successfully sorted!***')

# genre_sort('Coldplay', 'Yellow')