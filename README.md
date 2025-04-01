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

However, there is currently an issue with request timeouts, as we are currently making one incredibily long API request for all 500 artists. We will need to implement some form of tracker to continue searching from where we left off after a timeout.

## Authors

This project is a collaborative effort between Momoka Iwase, Tiffany Kwak, Brian Kwan, Ricardo Perez, and Andrew Pham.

## Sources

The top 500 artists are sourced from [this website](https://kworb.net/spotify/listeners.html).

## To Do

Implement a tracker to workaround API timeouts.