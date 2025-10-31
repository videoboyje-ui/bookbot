from stats import get_book_text, get_word_count, char_count

def main():
    book_file_path = "books/frankenstein.txt"
    
    # print total number of words in book
    num_words = get_word_count(get_book_text(book_file_path))
    print(f"Found {num_words} total words")
    
    # print dictionary with unique char and number of instances
    char_totals = char_count(get_book_text(book_file_path))
    print (char_totals)
    
    return

main()