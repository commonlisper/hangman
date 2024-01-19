import os
import words
import pics

ATTEMPTS = len(pics.FRAME)
WORDS_FILE_NAME = "nounlist.txt"


def greetings() -> None:
    msg = f"""Welcome to hangman game!

You must guess all letters in random word. Attemts number is {ATTEMPTS}.
The game lasts until you guess the word or until there are attempts left."""

    print(msg)


def display_game_status():
    raise NotImplementedError


def get_user_input() -> str:
    raise NotImplementedError


def game():
    greetings()
    random_word = words.random_word_from_file(f"{os.getcwd()}{os.sep}{WORDS_FILE_NAME}")
    guess_chars = ""
    player_word = words.get_masked_word(random_word, guess_chars)

    while random_word != player_word or ATTEMPTS:
        display_game_status()
        in_char = get_user_input()


def main():
    game()


if __name__ == "__main__":
    main()
