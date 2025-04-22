import csv

# Input and output file paths
input_file = 'streamedsongs421.csv'
output_file = 'streamedsongs421_titles.txt'


with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    titles = [row[0] for row in reader]

with open(output_file, 'w', encoding='utf-8') as txtfile:
    for title in titles:
        txtfile.write(title + '\n')
