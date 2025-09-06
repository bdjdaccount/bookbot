from stats import sort_dictionary, get_num_words, get_character_dictionary
import sys

if sys.argv and len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_location = sys.argv[1]

def get_book_text():
    with open(book_location) as f:
        return f.read()

def format_characters(a: list):
    for val in a:
        print(val["name"] + ": " + str(val["num"]))
    return print("============= END ===============")

def main():
    book_text = get_book_text()
    num_words = get_num_words(book_text)

    char_dict = get_character_dictionary(book_text)

    print(
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {book_location}...\n"
        f"----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        f"--------- Character Count -------"
    )
    print(format_characters(sort_dictionary(char_dict)))
    
main()

