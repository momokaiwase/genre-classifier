# genre-classifier


## Installation & Usage

All libraries that should be installed are in requirements.txt. Ensure you have the libraries installed:

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

## Authors

This project is a collaborative effort between Momoka Iwase, Tiffany Kwak, Brian Kwan, Ricardo Perez, and Andrew Pham.

## Sources

The top artists are sourced from [this website](https://kworb.net/spotify/listeners.html).

The top songs are sourced from [the same website as above](https://kworb.net/spotify/songs.html).

The documentation for the LyricsGenius library can be found [here](https://lyricsgenius.readthedocs.io/en/master/index.html).

TheAudioDB API's documentation can be found [here](https://www.theaudiodb.com/).

## To Do

**Solved 4/1/2025:** ~~Implement a tracker to workaround API timeouts.~~

**Solved 4/2/2025:** ~~Implement a way to keep the Genius search running even after a timeout.~~

**Solved 4/4/2025:** ~~Add a search limit to prevent infinitely searching an artist in case their search keeps timing out.~~

**Solved 4/9/2025:** ~~Scrape another 500 artists.~~

**Solved 4/9/2025:** ~~Added genre sort with known song tracker.~~

**Solved 4/14/2025:** ~~Genre classifying takes a really long time because of the method of search. We should try to find a better way to tag them, but with the specific tags that Genius gives us this may be difficult.~~

**Solved 4/15/2025:** ~~TheAudioDB API allows us to easily sort by genres; however, we are waiting on an API key to properly utilize it.~~

**Solved 4/16/2025:** ~~Add more songs to account for the amount that will need to be cut from the final dataset.~~

**Solved:** ~~Genre sort the new songs.~~

**TODO:** Update README and repository; comment code in `modeling/` and `dataset_raw_lyrics.py` in `functions/`. Look over File Hierarchy, especially for the CSV files left in the root directory.

## File Hierarchy

This is an overview of the files and directories in this repository.

### `classification/`

Directory containing different data classification methods.

#### `Bert.ipynb`

Jupyter Notebook file that builds a BERT model to classify song genres, and prints evaluation metrics.

#### `ffnn_bow.py`

Python file that builds a Feed Forward Neural Network model using bag of words to classify song genres, and prints evaluation metrics.

#### `ffnn_w2v.py`

Python file that builds a Feed Forward Neural Network model using word2vec word embeddings to classify song genres, and prints evaluation metrics.

#### `llm_classify.py`

Python file that builds a Mistral AI LLM model to classify song genres, and prints evaluation metrics.

#### `naivebayesbagofwords.ipynb`

Jupyter Notebook file that creates a Naive Bayes Bag of Words model.

#### `nb,baseline, and plots.ipynb`

Contains all metrics and plots for the Naive Bayes Bag of Words model.

#### `RNN Training.ipynb`

Jupyter Notebook file that intializes and trains the recurrent neural network.

#### `SVM_songs.ipynb`

Jupyter Notebook file that models the support vector machine.

#### `test_train_split.py`

Helper file that splits the dataset of untokenized lyrics into a 20/80 test/train split for the LLM and BERT Classifications.

#### `word2vec embedding.ipynb`

Jupyter Notebook file that models word2vec embeddings.

### `data exploration/`

Directory containing files relevant to data exploration.

#### `cluster_1_titles.txt`

Text file containing song titles in cluster 1.

#### `cluster_2_titles.txt`

Text file containing song titles in cluster 2.

#### `cluster_3_titles.txt`

Text file containing song titles in cluster 3.

#### `cluster_4_titles.txt`

Text file containing song titles in cluster 4.

#### `cluster_5_titles.txt`

Text file containing song titles in cluster 5.

#### `cluster_6_titles.txt`

Text file containing song titles in cluster 6.

#### `get_titles.py`

Python file that retrieves song titles from `streamedsongs421.csv` and saves them in `streamedsongs421_titles.txt`.

#### `lyric_LDA_cluster.py`

Python file that creates LDA clusters for song lyrics.

#### `streamedsongs421_titles.txt`

Text file containing all song titles.

#### `title_cluster.py`

Python file that creates k-means clusters for song titles.

### `dataset/`

Directory containing the dataset and any other relevant data.

#### `applying_genrelabels.ipynb`

Jupyter Notebook file that applies genre labels to songs.

#### `combining genre txt.ipynb`

Jupyter Notebook file that combines genres.

#### `known.txt`

Text file containing artists and songs that have already been searched.

#### `makingfinaldataset.ipynb`

Jupyter Notebook file that creates the final dataset.

#### `nlp project data tokenization and filtering-2.ipynb`

Jupyter Notebook file that tokenizes and filters song entries.

#### `nlp project data tokenization and filtering.ipynb`

Jupyter Notebook file that tokenizes and filters song entries.

#### `raw_lyrics_generelabel_int.csv`

CSV file with headers [Artist, Song Title, Genre, Lyrics, Genre_Label].

#### `raw_lyrics_generelabel.csv`

CSV file with headers [Artist, Song Title, Genre, Lyrics].

#### `raw_lyrics_test_dataset.csv`

CSV file that contains the raw lyrics of the testing data.

#### `raw_lyrics_train_dataset.csv`

CSV file that contains the raw lyrics of the training data.

#### `raw_lyrics.csv`

CSV file with headers [Artist, Song Title, Stemmed With Stop Words, Stemmed No Stop Words, Row_Index, Genre].

#### `ricardosongs422.csv`

CSV file containing a part of the dataset with headers [Artist, Song Title, Genre]

#### `song_chart.csv`

CSV file where each row is a song. The columns are as follows: Artist Name, Artist ID, Song Name, Song ID, Song Lyrics.

#### `songs_final422.csv`

CSV file with headers [Artist, Song Title, Stemmed With Stop Words, Stemmed No Stop Words, Row_Index, Genre], where the song title is tokenized.

#### `songs420_header.csv`

CSV file with headers [Artist, random, Song Title, random2, Lyrics].

#### `songs420.csv`

CSV file that is identical to `songs420_header.csv` without the header row.

#### `songs422.csv`

CSV file with headers [Artist, Song Title, Stemmed With Stop Words, Stemmed No Stop Words, Row_Index].

#### `streamedsongs421.csv`

CSV file with headers [Song Title, Stemmed], which contains songs and their stemmed lyrics.

#### `tiffanysongs422.csv`

CSV file with headers [Artist, Song Title, Genre].

#### `tokenized_dataset_genre_labels.csv`

CSV file with headers [Artist, Song Title, Stemmed With Stop Words, Stemmed No Stop Words, Row_Index, Genre, Genre_Label].

#### `top_spotify_artists.csv`

Text file that contains the top Spotify artists.

#### `top_spotify_songs.csv`

Text file countating the top 2500 Spotify songs.

### `functions/`

Directory containing essential functions.

#### `avg_token_per_song.py`

Python file that calculates the average token per song.

#### `chart_helper.py`

Python file that contains helper functions for creating the song chart.

#### `dataset_raw_lyrics.py`

Python file that generates the dataset of untokenized lyrics. Output is raw_lyrics_genrelabel.csv that has columns of Artist, Song Title, Genre, Lyrics.

#### `genre_mapping.py`

Python file that maps genre labels as strings into integers that tag each genre. Output is raw_lyrics_genrelabel_int.csv which is identical to raw_lyrics_genrelabel.csv except with an added column of Genre_Label with the integer tags of each genre.

#### `genre_sort.py`

Python file that sorts songs by their genre tag using TheAudioDB API.

#### `get_top.py`

Python file that scrapes the top Spotify artists and saves them in `top_500_spotify_artists.csv`. The number of artists saved is specified within the file.

#### `header.py`

Python file that duplicates `songs420.csv` with headers as `songs420_header.csv`.

#### `make_song_chart.py`

Python file that creates the song chart, saved in `song_chart.csv`.

### `genres/`

Directory containing respective genre directories.

#### `Country/`

Directory containing country songs.

#### `EDM/`

Directory containing EDM songs.

#### `Exclude/`

Directory containing excluded songs.

#### `Pop/`

Directory containing pop songs.

#### `R&B/`

Directory containing R&B songs.

#### `Rap/`

Directory containing rap songs.

#### `Rock/`

Directory containing rock songs.

### `requirements.txt`

Text file that contains the necessary libraries and versions.


