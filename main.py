from stats import word_count, character_count, get_book_text, sort_char_counts
import sys
import os

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ===========")
    print("Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f'Found {word_count(get_book_text(path))} total words')
    print("--------- Character Count -------")
    sorted_counts = sort_char_counts(character_count(get_book_text(path)))
    for char, count in sorted_counts.items():
        print(f"{char}: {count}")

main()
