from stats import get_book_text, get_words_count, get_characters_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    num_words = get_words_count(book_content)
    print(f"Found {num_words} total words")
    chars_count_main = get_characters_count(book_content)
    for item in chars_count_main:
        print(f"{item["char"]}: {item["num"]}")

main()