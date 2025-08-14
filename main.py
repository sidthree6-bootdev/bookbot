from stats import book_word_count, book_character_count, sort_character_dict

def get_book_text(filepath):
    with open(filepath) as file_content:
        return file_content.read()

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    book_word_count_value = book_word_count(book_text)

    # Report Print
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {book_word_count_value} total words")

    print("--------- Character Count -------")
    sorted_character_list = sort_character_dict(book_character_count(book_text))
    for char_info in sorted_character_list:
        if char_info['char'].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")

    print("============= END ===============")

main()