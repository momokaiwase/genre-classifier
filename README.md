# 🎵 NLP-Based Music Genre Classification

## Overview
This project leverages Natural Language Processing (NLP) and machine learning to classify songs into music genres based on their lyrics. We scraped data from Spotify's top artists and songs, then applied multiple classification models to determine how accurately song lyrics alone can predict genre.

View our final presentation slide deck:
📎 [Genre Classification - NLP final project.pptx.pdf](https://docs.google.com/presentation/d/125M_7E9piEraMPXuhHWmFXRcabdIL83A/edit?usp=sharing&ouid=112610846148247704192&rtpof=true&sd=true)

## 📂 Dataset
We built a custom dataset by scraping popular artist data from Spotify and pairing it with songs and lyrics with the Genius API along with genre information with the TheAudioDB API.

- Artists: Top 1,000 Spotify artists (scraped)
- Songs per Artist: ~15 songs each
- Lyrics: Collected via the Genius API using the LyricsGenius Python library
- Genres: Tagged using TheAudioDB API
- Final Dataset Size: ~10,000 entries
- Data Fields:
    - artist_name
    - song_title
    - lyrics
    - genre

This dataset captures a wide variety of mainstream music across multiple genres, making it suitable for supervised learning on lyrical genre classification.

## 🧠 Models Used
- Naive Bayes
- SVM
- Feed Forward NN
- Mistral LLM
- BERT

## 📊 Evaluation
We used accuracy, precision, recall, and F1-score to evaluate model performance across genres such as:
- Pop
- Hip-Hop
- Country
- Rock
- R&B

The best-performing model was Mistral with an accuracy of 68%.

## 📈 Results Snapshot
| Model                           | Accuracy | F1 Score |
| ------------------------------- | -------- | -------- |
| Stratified Baseline             | 24%      | 17%      |
| Naive Bayes                     | 53%      | 39%      |
| SVM                             | 50%      | 47%      |
| Feed Forward NN - bag of words  | 54%      | 46%      |
| Feed Forward NN - word2vec      | 53%      | 40%      |
| Mistral LLM                     | 68%      | 60%      |
| BERT                            | 65%      | 64%      |

## 🛠️ Tools & Libraries
**Data Processing & Analysis**: pandas, NumPy, SciPy, evaluate
**Natural Language Processing (NLP)**: Transformers, NLTK, Gensim, python-dotenv
**Machine Learning & Classification**: scikit-learn, MistralAI API, tensorflow
**Web Scraping & APIs**: requests, BeautifulSoup4, lyricsgenius  

## 💡 Key Insights
- Lyrics alone provide a strong signal for genre classification, especially for genres with distinctive vocabularies (e.g. rap).
- Simpler models like Naive Bayes perform decently well, but transformer-based models offer improved performance.
- Genre overlap and ambiguous lyrics can reduce classification accuracy.

## 🚀 How to Run
git clone https://github.com/your-repo/genre-classifier.git
cd genre-classifier
pip install -r requirements.txt

### Data Acquisiton & Enabling Genius Search

Create a [Genius API Client](https://genius.com/api-clients). Create an account if necessary, then fill in the App Name and App Website URL. You can use [localhost:6000](http://localhost:6000/) or another domain. You should now see an option to generate a Client Access Token. Click it to generate a token and copy it.

Create a file called `.env`. Within this file, create a variable called `CLIENT_TOKEN`. Paste the token you got as its value.

In order to sort songs by genre using `genre_sort.py`, you will need to add another field to the `.env` file called `DB_TOKEN`. TheAudioDB's API tokens are given by subscription, therefore there is no default token we can use. **If you want to run `genre_sort.py`, please contact Andrew Pham for access to the key.**

**DO NOT WRITE THE PRIVATE KEY INTO A PUBLICLY ACCESSIBLE FILE, IT SHOULD BE TAKEN FROM `.env`**.

Contents of `.env`:

    CLIENT_TOKEN = 'YOUR CLIENT ACCESS TOKEN'
    DB_TOKEN = 'YOUR THEAUDIODB ACCESS TOKEN'

### Data Collection

Currently, data collection relies on `top_spotify_artists.csv` and `functions/make_song_chart.py`. The CSV file contains the top artists on Spotify currently, scraped from [this website](https://kworb.net/spotify/listeners.html) using BeautifulSoup. `top_spotify_songs.csv` contains the top songs on Spotify currently, and is scraped from [the same website](https://kworb.net/spotify/songs.html). The number of artists is determined by the number specified in `functions/get_top.py`. It is currently set for 1000.

**Running `get_top.py` will generate `top_spotify_artists.csv` and `top_spotify_songs.csv`.**

`song_chart.csv` contains the data necessary for this project, containing (Artist Name, Artist ID, Song Name, Song ID, Song Lyrics).

`make_song_chart.py` tracks what artists have already been searched, so when run will continuously search the remaining artists. If a timeout occurs, it will restart the search for that artist. If 10 searches occur without a successful search, the artist is skipped.

It should be noted that some artists, like 50 Cent and Jay-Z, are unable to have full searches done on them for some reason; the API will keep timing out no matter how many times we try and search, therefore we are omitting these artists and any future artists that have the same issue.

**Running `make_song_chart.py` will generate `song_chart.csv`.**

`genre_sort.py` sorts all songs in `song_chart.csv` into the `genres/` directory, which contains text files named after TheAudioDB's genre tags.

**Running `genre_sort.py` will generate text files within the `genres/` directory.**

## Contributors

This project is a collaborative effort between Momoka Iwase, Tiffany Kwak, Brian Kwan, Ricardo Perez, and Andrew Pham.

## Sources

The top artists are sourced from [this website](https://kworb.net/spotify/listeners.html).

The top songs are sourced from [the same website as above](https://kworb.net/spotify/songs.html).

The documentation for the LyricsGenius library can be found [here](https://lyricsgenius.readthedocs.io/en/master/index.html).

TheAudioDB API's documentation can be found [here](https://www.theaudiodb.com/).

## File Hierarchy
<pre> 
├── classification/ # Genre classification models (BERT, FFNN, SVM, Naive Bayes, LLM) 
├── data exploration/ # Clustering and analysis of lyrics and song titles 
├── dataset/ # Raw and processed datasets, tokenization and labeling notebooks 
├── functions/ # Utility scripts for scraping, processing, and dataset management 
├── genres/ # Organized folders for different song genres (Pop, Rap, Rock, etc.) 
├── requirements.txt # Python dependencies 
└── README.md 
</pre>
