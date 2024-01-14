import os
import words

WORDS_FILE_NAME = "nounlist.txt"


def game():
    # greetings()
    random_word = words.random_word_from_file(f"{os.getcwd()}{os.sep}{WORDS_FILE_NAME}")
    guess_chars = ""
    player_word = words.get_masked_word(random_word, guess_chars)


def main():
    game()


if __name__ == "__main__":
    main()
