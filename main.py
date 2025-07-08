from stats import word_count, character_count, get_book_text, sort_char_counts
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py books/<book_filename.txt>")
        return
    
    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"Error: File not found at path '{path}'")
        return
    print("============ BOOKBOT ===========")
    print("Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f'Found {word_count(get_book_text(path))} total words')
    print("--------- Character Count -------")
    sorted_counts = sort_char_counts(character_count(get_book_text(path)))
    for char, count in sorted_counts.items():
        print(f"{char}: {count}")

main()
