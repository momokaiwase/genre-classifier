### Sorts songs by genre tag various text documents.
from dotenv import load_dotenv
from lyricsgenius import Genius
import chart_helper as ch
import os
import requests
from bs4 import BeautifulSoup

# Loads .env, which contains the client token
load_dotenv()

BASE_URL = "https://api.genius.com"

# Initializes the Genius API client token
client_token = os.getenv("CLIENT_TOKEN")

# Initizalizes Genius search
genius = Genius(client_token)

# Function to get song tags from Genius
def get_song_url(song_title):

    # Song ID (example: 96183 for 'Young Girls' by Bruno Mars)
    song_id = 96183

    # Headers including your API token for authentication
    headers = {
        "Authorization": f"Bearer {client_token}"
    }

    # Get song ID
    # Send GET request to search for the song by title
    response = requests.get(f"{BASE_URL}/search", params={"q": song_title}, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        search_results = response.json()['response']['hits']
        if search_results:
            # Get the first song result
            song = search_results[0]['result']
            song_id = song['id']
            song_title = song['title']
            artist_name = song['primary_artist']['name']
            print("song ID successfully fetched!")
            print(f"Song Title: {song_title}\nArtist: {artist_name}\nSong ID: {song_id}")

            song_url = song['url']  # Get the song URL from search result
            print(f"Song URL: {song_url}")
            return song_url

        else:
            print(f"No data results found for '{song_title}'.")
    else:
        print(f"Error: {response.status_code}")

def get_song_tags(song_url):
    url = song_url

    # Make a GET request to the song's Genius page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Look for tag elements on the page (tags are typically found under a specific div or span)
    # This is just an example, you may need to adjust the selector
    tags = soup.find_all('a', class_='tag')

    # Print the tags found
    for tag in tags:
        print(tag.get_text())
    
    # Return tags in a list if needed
    return [tag.get_text() for tag in tags]


### Given a list of song names, sorts songs by genre in their respective text files in the genres/ folder
def genre_sort(songs):

    # Genre tags
    genres = ['rap', 'pop', 'r-b', 'rock', 'country', 'non-music']

    # Stores the final genre dictionary
    # genre_dict = {'rap':[], 'pop':[], 'r-b':[], 'rock':[], 'country':[], 'non-music':[]}

    # Creates list of sorted songs
    sorted_songs = []
    files = ['genres/rap.txt', 'genres/pop.txt', 'genres/r-b.txt', 'genres/rock.txt', 'genres/country.txt', 'genres/non-music.txt', 'genres/failed.txt']
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as known:
            # Move file pointer to beginning for reading
            known.seek(0, 0)

            sorted_songs.extend(known.readlines())

    print(sorted_songs)

    # Iterate through the songs. For each song, continue searching each tag until a hit is found.
    for song in songs:
        # If the song has already been sorted, skip it
        if song + '\n' in sorted_songs:
            print(f"---{song} has already been tagged.---")
            continue

        # Tracks whether the song has been tagged
        tagged = False

        #get tags for that specific song
        print(f"getting tags for {song}")
        song_tags = get_song_tags(get_song_url(song))
        print(song_tags)
        for tag in song_tags:
            if tag in genres:
                print(f"---Hit found! {song} is genre: {tag}---")

                # Append the song to the genre text file
                with open(f'genres/{tag}.txt', 'a', encoding='utf-8') as genre_file:
                    genre_file.write(song + '\n')
                tagged = True
                break
            else:
                print(f"---Failed to find hit for {song}.---")

        if not tagged:
            print(f"---Search for {song} failed. Adding to failed.txt.---")
            with open('genres/failed.txt', 'a', encoding='utf-8') as failed:
                failed.write(song + '\n')

        print(f"---{song} has been successfully tagged!---")

    print("---Sorting completed.---")
    # return genre_dict
            
# Retrieves the first 500 artists and their songs
artists = ch.get_names("top_spotify_artists.csv")[0:500] 
songs = ch.get_titles(artists)

genre_sort(songs)

### Debug to ensure tagging actually works.
# genre_sort(['DNA.'])