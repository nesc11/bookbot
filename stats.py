def count_words(book_text):
    words = book_text.split()
    return len(words)


def make_characters_dict(book_text):
    characters_dict = {}
    for char in book_text.lower():
        if characters_dict.get(char) is None:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict


def make_characters_list(characters_dict):
    characters_list = [
        {"char": key, "num": value} for key, value in characters_dict.items()
    ]
    characters_list.sort(reverse=True, key=lambda x: x["num"])
    return characters_list
