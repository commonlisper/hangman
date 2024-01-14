import random

MASKED_CHAR = "-"


def random_word_from_file(filepath):
    """Return random word from file

    Args:
        filepath (str): path to the file with words

    Returns:
        str: single word from file
    """
    with open(filepath, "r", encoding="utf-8") as file:
        words = [ln for line in file if len(ln := line.strip()) > 4]

    word = words[random.randint(0, len(words))]
    return word


def get_masked_word(random_word, guess_chars):
    """Get masked word with masked char that corresponding to guess word

    Args:
        random_word (str): random word that computer wished
        guess_chars (str): string with guess letters

    Returns:
        str: masked word
    """

    masked_word = "".join(
        [char if char in guess_chars
         else MASKED_CHAR
         for char in random_word
         ]
    )

    return masked_word
