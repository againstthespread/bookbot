from stats import word_count
from stats import character_count
from stats import get_book_text

def main():
    print(character_count(get_book_text("books/frankenstein.txt")))

main()
