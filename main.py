import sys

from stats import num_of_words
from stats import num_of_characters


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]


def get_book_text():
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_of_words(text)
    print("--------- Character Count -------")
    num_of_characters(text)


main()

