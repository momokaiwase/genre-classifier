import csv
import ast

def calculate_average_tokens(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        total_tokens_with_stop_words = 0
        total_tokens_no_stop_words = 0
        row_count = 0
        
        for row in reader:
            try:
                # Convert string representation of lists to actual lists
                tokens_with_stop_words = ast.literal_eval(row['Stemmed With Stop Words'])
                tokens_no_stop_words = ast.literal_eval(row['Stemmed No Stop Words'])
                
                total_tokens_with_stop_words += len(tokens_with_stop_words)
                total_tokens_no_stop_words += len(tokens_no_stop_words)
                row_count += 1
            except (ValueError, KeyError):
                print(f"Skipping row {row}: Unable to parse tokens")
        
        # Calculate averages
        avg_tokens_with_stop_words = total_tokens_with_stop_words / row_count if row_count > 0 else 0
        avg_tokens_no_stop_words = total_tokens_no_stop_words / row_count if row_count > 0 else 0
        
        return avg_tokens_with_stop_words, avg_tokens_no_stop_words

# Example usage:
file_path = 'songs_final422.csv'
avg_with_stop, avg_no_stop = calculate_average_tokens(file_path)
print(f"Average tokens with stop words: {avg_with_stop}")
print(f"Average tokens without stop words: {avg_no_stop}")
