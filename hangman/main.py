import os

import console_ui as cui
import state
import words
from answer import Answer


def run_game_loop() -> None:
    attempts = len(state.HANGMAN_STATE) - 1
    words_file = "nounlist.txt"
    masked_letter = "-"
    min_word_len = 4
    max_word_len = len(state.HANGMAN_STATE) + 2

    cui.show_welcome_message(attempts)

    while True:
        filepath = f"{os.getcwd()}{os.sep}{words_file}"
        word = words.get_random_word(filepath, min_word_len, max_word_len)
        entered_letters: list[str] = []

        guessed_word, attempts_count = play_game_session(attempts, masked_letter, word, entered_letters)

        if word == guessed_word:
            cui.show_win_message()
        elif attempts_count == attempts:
            cui.show_lost_message()

        cui.show_user_statistic(word, guessed_word, entered_letters, attempts_count)

        if cui.request_user_answer() == Answer.NO.value:
            cui.show_goodbye_message()
            break


def play_game_session(
    attempts: int,
    masked_letter: str,
    word: str,
    entered_letters: list[str],
) -> tuple[str, int]:
    guessed_word = words.make_masked_word(word, entered_letters, masked_letter)
    attempts_count = 1

    while guessed_word != word and attempts_count <= attempts:
        cui.show_game_status(attempts_count, guessed_word, entered_letters)

        input_letter = cui.request_user_letter(entered_letters)
        entered_letters.append(input_letter)
        guessed_word = words.make_masked_word(word, entered_letters, masked_letter)

        if input_letter not in word:
            if attempts_count == attempts:
                break

            attempts_count += 1

    return guessed_word, attempts_count


if __name__ == "__main__":
    run_game_loop()
