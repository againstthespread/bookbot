def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents2 = file_contents.lower()
        return file_contents2

def word_count():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_counts(char_dict):
    # Filter to keep only alphanumeric characters
    filtered_items = [(char, count) for char, count in char_dict.items() if char.isalpha()]
    # Sort by count descending using .sort()
    filtered_items.sort(key=lambda x: x[1], reverse=True)
    # Convert back to dictionary if needed
    sorted_dict = dict(filtered_items)
    return sorted_dict


