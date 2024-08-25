from typing import Dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    number_of_characters = count_characters(text)
    print(f"{number_of_words} words found in the document")
    generate_report(number_of_characters)


def generate_report(characters) -> Dict[str, int]:
    characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    for k, v in characters.items():
        print(f"The '{k}' character appears {v} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters


if __name__ == "__main__":
    main()
