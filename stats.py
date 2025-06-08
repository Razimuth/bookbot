def number_of_words(contents_of_file):
    word_count = 0
    # splits file into list of words
    words = contents_of_file.split(None,-1)
    for word in words:
        word_count += 1
    return word_count

def count_characters(contents_of_file):
    characters = {}
    for char in contents_of_file:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    return characters

#def sorted_characters(characters_dict):
#    sorted_dict = characters_dict.sort()
    
#    return sorted_dict 

#Add a new function to your stats.py file that takes the dictionary of characters and their counts and 
# returns a sorted list of dictionaries.
#Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
#Sort the list from greatest to least by the count.
#The .sort() method will be helpful here (see the hint).

 #Here's an example of how you can use the .sort() method to sort a list of dictionaries:

 # A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
"""def sort_on(dict):
    return dict["num"]

vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]
vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
"""