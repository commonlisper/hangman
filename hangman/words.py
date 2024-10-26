import random


def get_random_word(filepath: str, min_word_len: int, max_word_len: int) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        words = [w for word in file if min_word_len < len(w := word.strip()) <= max_word_len]

    return random.choice(words)


def make_masked_word(word: str, entered_letters: list[str], masked_letter: str) -> str:
    masked_word = "".join([letter if letter in entered_letters else masked_letter for letter in word])

    return masked_word
