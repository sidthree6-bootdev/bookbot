def get_book_text(filepath):
    with open(filepath) as file_content:
        return file_content.read()

def book_word_count(book_text):
    words = book_text.split()
    return len(words)

def main():
    book_text = get_book_text('books/frankenstein.txt')
    book_word_count_value = book_word_count(book_text)
    print(f"{book_word_count_value} words found in the document")

main()