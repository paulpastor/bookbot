import sys

from stats import char_acount_alpha_only_sorted, count_characters, count_words

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_fp = sys.argv[1]


def get_book_text(fp):
    with open(fp) as f:
        return f.read()


def main():
    book_text = get_book_text(book_fp)

    count = count_words(book_text)
    print(f"Found {count} total words")

    char_count = count_characters(book_text)
    char_count_sorted = char_acount_alpha_only_sorted(char_count)
    for char in char_count_sorted:
        print(f"{char['char']}: {char['num']}")


main()
