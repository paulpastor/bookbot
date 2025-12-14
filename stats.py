def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict:
    char_count = {}
    for character in text:
        character = character.lower()
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count


def sort_on(items):
    return items["num"]


def char_acount_alpha_only_sorted(char_count: dict) -> list:
    char_count_list = []
    for key in char_count:
        if key.isalpha():
            new_dict = {"char": key, "num": char_count[key]}
            char_count_list.append(new_dict)
    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list
