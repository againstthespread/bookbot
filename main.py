from stats import word_count
from stats import character_count
from stats import get_book_text
from stats import sort_char_counts

def main():
    print("============ BOOKBOT ===========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {word_count()} total words')
    print("--------- Character Count -------")
    sorted_counts = sort_char_counts(character_count(get_book_text("books/frankenstein.txt")))
    for char, count in sorted_counts.items():
        print(f"{char}: {count}")

main()
