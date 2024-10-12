import random
import state

MASKED_SYMBOL = "-"
MIN_WORD_LEN = 4
MAX_WORD_LEN = len(state.HANGMAN_STATE) + 2


def get_random_word(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        words = [
            w
            for line in file
            if len(w := line.strip()) > MIN_WORD_LEN and len(w) <= MAX_WORD_LEN
        ]

    word = random.choice(words)
    return word


def make_masked_word(target_word: str, entered_letters: list[str]) -> str:
    masked_word = "".join(
        [
            letter if letter in entered_letters else MASKED_SYMBOL
            for letter in target_word
        ]
    )

    return masked_word
