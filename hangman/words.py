import random
import state

MASKED_SYMBOL = "-"
MIN_WORD_LEN = 4
MAX_WORD_LEN = len(state.HANGMAN_STATE)


def get_random_word(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        words = [
            w
            for line in file
            if len(w := line.strip()) > MIN_WORD_LEN and len(w) <= MAX_WORD_LEN
        ]

    word = words[random.randint(0, len(words))]
    return word


def make_masked_word(target_word: str, entered_letters: list[str]) -> str:
    masked_word = "".join(
        [char if char in entered_letters else MASKED_SYMBOL for char in target_word]
    )

    return masked_word
