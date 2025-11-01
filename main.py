from stats import get_book_text, get_word_count, char_count, sort_char_analysis
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    book_file_path = sys.argv[1]
    
    # print total number of words in book
    num_words = get_word_count(get_book_text(book_file_path))
        
    # print dictionary with unique char and number of instances
    char_totals = char_count(get_book_text(book_file_path))

    # Generate Pretty Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_char_analysis(char_totals)
    print("============= END ===============")

    return



main()