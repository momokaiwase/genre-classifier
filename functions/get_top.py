# Generates the top_spotify_artists.csv file
from bs4 import BeautifulSoup
import requests
import csv

### Scrapes the top num artists from the below URL and stores them in a csv file
def get_top(num):
    url = 'https://kworb.net/spotify/listeners.html'

    # Sends HTTP GET request
    response = requests.get(url)

    # Raise exception for HTTP errors
    response.raise_for_status()  

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find table containing artist data
    table = soup.find('table')

    # List of tuples that stores extracted data
    artists_data = []

    # Iterate over the rows of the table
    for row in table.find_all('tr')[1:num+1]:  # Skip header and limit to num + 1 rows
        columns = row.find_all('td')
        rank = columns[0].get_text()
        artist_name = columns[1].get_text()
        monthly_listeners = columns[2].get_text()

        # print(columns)
        # print(rank)
        # print(artist_name)
        # print(monthly_listeners)

        # Append extracted data as a tuple
        artists_data.append((int(rank), artist_name, int(monthly_listeners.replace(",", ""))))

    # print(artists_data)

    # Save data to a CSV file
    with open('top_spotify_artists.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Rank', 'Artist Name', 'Monthly Listeners'])
        writer.writerows(artists_data)

    print('top_spotify_artists.csv saved successfully!')

### Scrapes individual songs
def get_songs(num):
    url = 'https://kworb.net/spotify/songs.html'

    # Sends HTTP GET request
    response = requests.get(url)

    # Raise exception for HTTP errors
    response.raise_for_status()  

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find table containing artist data
    table = soup.find('table')

    # List of tuples that stores extracted data
    song_data = []

    # Stores progress
    rank = 1

    # Iterate over table
    for row in table.find_all('tr')[1:num-1]:
        columns = row.find_all('td')
        rank = rank
        data = columns[0].get_text().split(' - ')
        artist_name = data[0]
        song_name = data[1]

        # print(columns)
        # print(rank)
        # print(data)
        # print(artist_name)
        # print(song_name)

        print(f'{rank}/2500')
        rank += 1

        # Append extracted data as a tuple
        song_data.append((int(rank), artist_name, song_name))

    # Save data to a CSV file
    with open('top_spotify_songs.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Rank', 'Artist Name', 'Song Name'])
        writer.writerows(song_data)

    print('top_spotify_songs.csv saved successfully!')


# get_top(1000)
get_songs(2500) # Maximum value: 2500