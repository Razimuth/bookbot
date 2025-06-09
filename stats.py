def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_by(item):
    return item["num"]

def get_sorted_list(char_dict):
    list_of_dict = []
    for char in char_dict:
        dict = {"name": char, "num": char_dict[char]}
        list_of_dict.append(dict)
    list_of_dict.sort(reverse=True, key=sort_by)
    return list_of_dict

