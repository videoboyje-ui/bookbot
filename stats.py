def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def char_count(text):
    # Convert the text string to all lowercase.
    shrunk_text = text.lower()
    
    # Initialize a dictonary to hold all unique characters (key) and their count (Value).
    char_totals = {}

    # Iterate through every character in "text".
    for x in range(len(shrunk_text)):
        # If char (Key) exist increment count (Value) by 1.
        if shrunk_text [x] in char_totals:
            char_totals[shrunk_text[x]] = char_totals[shrunk_text[x]] + 1
        # If char does not exist then add it (Key) and set the count to 1 (Value)
        if shrunk_text[x] not in char_totals:
            char_totals[shrunk_text[x]] = 1

    return char_totals