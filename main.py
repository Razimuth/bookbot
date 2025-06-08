from stats import number_of_words
from stats import count_characters
#from stats import sorted_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    book_path = "/home/raz415/workspace/github.com/Razimuth/bookbot/books/frankenstein.txt"
      
    number_words = number_of_words(get_book_text(book_path))
    print(f"{number_words} words found in the document")

    character_count = count_characters(get_book_text(book_path))
    print(character_count) # Prints the char and its value

#    sorted_dictionay = sorted_characters(character_count)

#Import and call the function in main.py, and capture the result.
#Print the report to the console as shown above. If the character is not an alphabetical character 
# (using the .isalpha() method), just skip it.

main()


