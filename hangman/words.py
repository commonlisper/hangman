import random


def get_random_word(filepath: str, min_word_len: int, max_word_len: int) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        words = [w for line in file if min_word_len < len(w := line.strip()) <= max_word_len]

    word = random.choice(words)
    return word


def make_masked_word(target_word: str, entered_letters: list[str], masked_letter: str) -> str:
    masked_word = "".join(
        [letter if letter in entered_letters else masked_letter for letter in target_word]
    )

    return masked_word
