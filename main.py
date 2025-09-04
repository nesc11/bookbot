import sys
from stats import count_words, make_characters_dict, make_characters_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    characters_dict = make_characters_dict(book_text)
    charcaters_list = make_characters_list(characters_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in charcaters_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()
