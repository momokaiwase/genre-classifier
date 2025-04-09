### Sorts songs by genre tag.
from dotenv import load_dotenv
from lyricsgenius import Genius
import chart_helper as ch
import csv
import os

# Loads .env, which contains the client token
load_dotenv()

# Initializes the Genius API client token
client_token = os.getenv("CLIENT_TOKEN")

### Given a list of song names, returns a dictionary where each key is a genre tag, and each key's value is a list of songs within that genre
def genre_sort(songs):
    # Initizalizes Genius search
    genius = Genius(client_token)

    # Genre tags
    tags = ['rap', 'pop', 'r-b', 'rock', 'country', 'non-music']

    # Stores the final genre dictionary
    genre_dict = {'rap':[], 'pop':[], 'r-b':[], 'rock':[], 'country':[], 'non-music':[]}

    # Iterate through the songs. For each song, continue searching each tag until a hit is found.
    for song in songs:
        # Tracks whether the song has been tagged
        tagged = False

        # Begins at page 1 of the search
        page = 1

        while page and not tagged:
            print(f"---Current Page: {page}---")

            # Search each genre tag
            rap_res = genius.tag(tags[0], page=page)
            # Searches the tag results for the song
            print("---Searching rap...---")
            for hit in rap_res['hits']:
                print(hit)
                # If the song is within the genre tag, append it to the respective genre_dict key
                if hit['title'] == song:
                    print("---Hit found in rap!---")
                    genre_dict['rap'].append(song)
                    tagged = True
                else:
                    print("---Failed to find hit in rap.---")

            pop_res = genius.tag(tags[1], page=page)
            # Searches the tag results for the song
            print("---Searching pop...---")
            for hit in pop_res['hits']:
                print(hit)
                # If the song is within the genre tag, append it to the respective genre_dict key
                if hit['title'] == song:
                    print("---Hit found in pop!---")
                    genre_dict['pop'].append(song)
                    tagged = True
                else:
                    print("---Failed to find hit in pop.---")

            rb_res = genius.tag(tags[2], page=page)
            # Searches the tag results for the song
            print("---Searching r-b...---")
            for hit in rb_res['hits']:
                print(hit)
                # If the song is within the genre tag, append it to the respective genre_dict key
                if hit['title'] == song:
                    print("---Hit found in r-b!---")
                    genre_dict['r-b'].append(song)
                    tagged = True
                else:
                    print("---Failed to find hit in r-b.---")

            rock_res = genius.tag(tags[3], page=page)
            # Searches the tag results for the song
            print("---Searching rock...---")
            for hit in rock_res['hits']:
                print(hit)
                # If the song is within the genre tag, append it to the respective genre_dict key
                if hit['title'] == song:
                    print("---Hit found in rock!---")
                    genre_dict['rock'].append(song)
                    tagged = True
                else:
                    print("---Failed to find hit in rock.---")

            country_res = genius.tag(tags[4], page=page)
            # Searches the tag results for the song
            print("---Searching country...---")
            for hit in country_res['hits']:
                print(hit)
                # If the song is within the genre tag, append it to the respective genre_dict key
                if hit['title'] == song:
                    print("---Hit found in country!---")
                    genre_dict['country'].append(song)
                    tagged = True
                else:
                    print("---Failed to find hit in country.---")

            non_res = genius.tag(tags[5], page=page)
            # Searches the tag results for the song
            print("---Searching non-music...---")
            for hit in non_res['hits']:
                print(hit)
                # If the song is within the genre tag, append it to the respective genre_dict key
                if hit['title'] == song:
                    print("---Hit found in non-music!---")
                    genre_dict['non-music'].append(song)
                    tagged = True
                else:
                    print("---Failed to find hit in non-music.---")

            page += 1

        print(f"---{song} has been successfully tagged!---")

    return genre_dict
            
# Retrieves the first 500 artists and their songs
artists = ch.get_names("top_spotify_artists.csv")[0:500] 
songs = ch.get_titles(artists)

print(genre_sort(songs))

### Debug to ensure tagging actually works. Running the below should find a hit on the 2nd page, then should output the dictionary with 'DNA.' in the rap key.  
# print(genre_sort(['DNA.'])) 