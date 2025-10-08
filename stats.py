from collections import defaultdict

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def get_words_count(book_content):
    words_list = book_content.split()
    words_count = len(words_list)
    return words_count

def get_characters_count(book_content):
    char_counts = defaultdict(int)
    words_list = book_content.lower().split()
    for word in words_list:
        for char in word:
            if char.isalpha():
                char_counts[char] += 1
    
    # Convert to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    
    # Sort using sort_on function
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
def sort_on(items):
    return items["num"]



