# genre-classifier


## Installation & Usage

Ensure you have the following libraries installed:

    pip install requests
    pip install beautifulsoup4
    pip install lyricsgenius
    pip install dotenv

### Data Acquisiton & Enabling Genius Search

Create a [Genius API Client](https://genius.com/api-clients). Create an account if necessary, then fill in the App Name and App Website URL. You can use [localhost:6000](http://localhost:6000/) or another domain. You should now see an option to generate a Client Access Token. Click it to generate a token and copy it.

Create a file called `.env`. Within this file, create a variable called `CLIENT_TOKEN`. Paste the token you got as its value.

Contents of `.env`:

    CLIENT_TOKEN = 'YOUR CLIENT ACCESS TOKEN'

### Data Collection

Currently, data collection relies on `top_500_spotify_artists.csv` and `functions/make_song_chart.py`. The CSV file contains the top 500 artists on Spotify currently, scraped from [this website](https://kworb.net/spotify/listeners.html) using BeautifulSoup. `functions/get_top_500.py` can be run to update the CSV file.


## Authors

This project is a collaborative effort between Momoka Iwase, Tiffany Kwak, Brian Kwan, Ricardo Perez, and Andrew Pham.

## Sources

The top 500 artists are sourced from [this website](https://kworb.net/spotify/listeners.html).

## To Do

**Solved 4/1/2025:** ~~Implement a tracker to workaround API timeouts.~~

API request timeouts are still an issue, though we are not repeating searches. Searches simply do not complete sometimes; we may need to adjust song searches per author to limit request time.

## File Hierarchy

This is an overview of the files and directories in this repository.

### `functions`

Directory containing essential functions.

#### `chart_helper.py`

Python file that contains helper functions for creating the song chart.

#### `get_top_500.py`

Python file that scrapes the top 500 Spotify artists and saves them in `top_500_spotify_artists.csv`.

#### `make_song_chart.py`

Python file that creates the song chart, saved in `song_chart.csv`.

### `known.txt`

Text file containing artists that have already been searched.

### `song_chart.csv`

CSV file where each row is a song. The columns are as follows: Artist Name, Artist ID, Song Name, Song ID, Song Lyrics.

### `top_500_spotify_artists.csv`

Text file that contains the top 500 Spotify artists.