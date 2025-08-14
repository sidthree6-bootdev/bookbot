from stats import book_word_count

def get_book_text(filepath):
    with open(filepath) as file_content:
        return file_content.read()

def main():
    book_text = get_book_text('books/frankenstein.txt')
    book_word_count_value = book_word_count(book_text)
    print(f"{book_word_count_value} words found in the document")

main()