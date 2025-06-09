from stats import (get_num_words, get_chars_dict, get_sorted_list)
import sys

def main():
    home_path = "/home/raz415/workspace/github.com/Razimuth/bookbot/"
    book_path = get_book_path()
#    book_path = "books/frankenstein.txt"
    text = get_book_text(home_path + book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = get_sorted_list(chars_dict)
    print_report(book_path, num_words, sorted_list)

def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
    return book

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_list):
    print("=========== BOOKBOT =============")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for char in sorted_list:
        if char["name"].isalpha():
            print(f"{char["name"]}: {char["num"]}")
    print("============= END ===============")

main()
