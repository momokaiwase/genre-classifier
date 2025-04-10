### Sorts songs by genre tag various text documents.
from dotenv import load_dotenv
from lyricsgenius import Genius
import chart_helper as ch
import os

# Loads .env, which contains the client token
load_dotenv()

# Initializes the Genius API client token
client_token = os.getenv("CLIENT_TOKEN")

### Given a list of song names, sorts songs by genre in their respective text files in the genres/ folder
def genre_sort(songs):
    # Initizalizes Genius search
    genius = Genius(client_token)

    # Genre tags
    tags = ['rap', 'pop', 'r-b', 'rock', 'country', 'non-music']

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

        # Begins at page 1 of the search
        page = 1

        while page <= 50 and not tagged: # Genius will not return results after the 50th page
            print(f"---Current Page: {page}---")

            # Search each genre tag
            for tag in tags:
                print(f"---Searching {tag}...---")
                res = genius.tag(tags[0], page=page)
            
                # Searches the tag results for the song
                
                for hit in res['hits']:
                    # print(hit)
                    # If the song is within the genre tag, write it to the respective genre text file
                    if hit['title'] == song:
                        print(f"---Hit found in {tag}!---")

                        # Append the song to the genre text file
                        with open(f'genres/{tag}.txt', 'a', encoding='utf-8') as genre_file:
                            genre_file.write(song + '\n')
                        tagged = True
                        break
                    else:
                        print(f"---Failed to find hit in {tag}.---")
                
                page += 1

        # Add song to failed search text document if not found within 50 pages
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