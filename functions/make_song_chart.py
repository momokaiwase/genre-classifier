### Adds song chart rows to the song chart. Checks to ensure an artist is not repeated.
import csv
import chart_helper as ch
import os
import pathlib

# Redirects to root path
file_path = os.path.abspath('.') + ('/')

### Given a name, writes the assoicated rows to the song chart
def write_row(name):
    # Gets the artist's row
    row = ch.get_artist_data(name)

    # Append data to a CSV file
    with open('song_chart.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(row)

    # Confirmation
    print('song_chart.csv appended successfully!')

    # Adds artist name to known.txt
    with open('known.txt', 'a+', encoding='utf-8') as known:
        known.write(name + '\n')

    # Confirmation
    print('known.txt appended successfully!')

# Opens and stores all known artist names
with open('known.txt', 'r', encoding='utf-8') as known:
    # Move file pointer to beginning
    known.seek(0, 0)
    
    # List of all known names
    known_names = known.readlines()
    
# print(known_names)

# Loops through all 500 artists
for name in ch.get_names('top_500_spotify_artists.csv'):
    # Checks if the name is in known.txt, i.e. it has already been added to the chart
    if name + '\n' in known_names:
        print(f'{name} has already been recorded.')

    else:
        write_row(name)