### Adds song chart rows to the song chart. Checks to ensure an artist is not repeated.
import csv
import chart_helper as ch
import os

# Redirects to root path
file_path = os.path.abspath('.') + ('/') # I don't think we actually need this but I'm too afraid of deleting it and fucking something up

### Given a name, writes the assoicated rows to the song chart
def write_row(name, search_type):
    # Depending on the search type, retrieves the object's row data
    if search_type == 'artist': 
        row = ch.get_artist_data(name)
    
    elif search_type == 'song':
        row = ch.get_song_data(name)

    # Escape case if there is an infinite search loop
    if row == False:
        return f"---{name} could not be searched.---"

    # Append data to a CSV file
    with open('song_chart.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(row)

    # Confirmation
    print('---song_chart.csv appended successfully!---')

    # Adds name to known.txt
    with open('known.txt', 'a+', encoding='utf-8') as known:
        known.write(name + '\n')

    # Confirmation
    print('---known.txt appended successfully!---')

# Opens and stores all known artist names
with open('known.txt', 'r', encoding='utf-8') as known:
    # Move file pointer to beginning
    known.seek(0, 0)
    
    # List of all known names
    known_names = known.readlines()

# Stores known songs
known_songs = []

# Opens and stores all recorded song_chart.csv songs
with open('song_chart.csv', 'r', encoding='utf-8') as known:
    # Move fp to beginning
    known.seek(0, 0)

    # Appends all recorded songs to known_songs
    csvreader = csv.reader(known)
    for row in csvreader:
        known_songs.append(row[2])

print(known_songs)
    
# print(known_names)

# List containing artist names that should be skipped. Add any artist names that cannot search fully.
skip = ['50 Cent', 'JAY-Z', 'The Notorious B.I.G.', 'Dr. Dre', 'George Michael']


### Search by artist
# Loops through all artists
# for name in ch.get_names('top_spotify_artists.csv'):
#     # Checks if the name is in known.txt, i.e. it has already been added to the chart
#     if name + '\n' in known_names:
#         print(f'---{name} has already been recorded.---')

#     else:
#         if name in skip:
#             print(f'---Skipping {name}---')
#             continue
#         write_row(name, 'artist')
#         print(f'---Rows for {name} have been successfully recorded!---')


### Search by song
# Progress
prog = 1

# Stores all names
names = ch.get_all_songs()

# Loops through all song titles
for name in names:
    print(f'***{prog}/{len(names)}***')

    if name in known_songs:
        print(f'---{name} has already been recorded.---')
        prog += 1

    else:
        write_row(name, 'song')
        print(f'---The row for {name} has been successfully recorded!---')
        prog += 1