def book_word_count(book_text):
    words = book_text.split()
    return len(words)

def book_character_count(book_text):
    return_dict = {}

    for char in book_text:
        char = char.lower()
        if char in return_dict:
            return_dict[char] += 1
        else:
            return_dict[char] = 1

    return return_dict

def sort_character_dict(char_count_dict):
    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list