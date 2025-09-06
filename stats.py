def get_num_words(text):
    return len(text.split())

def get_character_dictionary(text: str) -> dict:
    char_dict = {}
    for char in text:
        char = char.lower()
        if char_dict.get(char) is None:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(items): 
    return items["num"]

def sort_dictionary(dictionary: dict) -> list:
    dict_list = []
    for a in dictionary:
        if a.isalpha() is True:
            cool = {
                "name": a,
                "num": dictionary[a]
            }
            dict_list.append(cool)
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list