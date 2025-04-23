import csv

# Genre mapping
genre_mapping = {
    "Pop": 0,
    "Rock": 1,
    "R&B": 2,
    "Country": 3,
    "EDM": 4,
    "Rap": 5
}

# Input and output file names
input_file = "songs_final422.csv"  # Replace with the actual input file name
output_file = "genre_as_numbers.csv"

# Read and process the data
with open(input_file, mode="r", encoding="utf-8") as infile, open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
    reader = csv.DictReader(infile, delimiter=",")
    fieldnames = reader.fieldnames + ["Genre_Label"]  # Add new column for labeled genre
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter="\t")
    
    # Write header
    writer.writeheader()
    
    # Process and write rows
    for row in reader:
        genre = row["Genre"]
        row["Genre_Label"] = genre_mapping.get(genre, -1)  # Use -1 for unknown genres
        writer.writerow(row)

print(f"Data has been processed and saved to {output_file}")


