import random


def random_word_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        words = [ln for line in file if len(ln := line.strip()) > 4]

    word = words[random.randint(0, len(words))]
    return word
