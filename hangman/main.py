import os
import words
import state
import messages
import cui


def game():
    attempts = len(state.HANGMAN_STATE)
    words_file = "nounlist.txt"

    messages.show_welcome_message(attempts)

    while True:
        filepath = f"{os.getcwd()}{os.sep}{words_file}"
        word = words.get_random_word(filepath)
        entered_letters = []
        guessed_word = words.make_masked_word(word, entered_letters)
        attempts_count = 1

        while guessed_word != word and attempts_count <= attempts:
            cui.show_game_status(attempts_count, guessed_word, entered_letters)

            input_letter = cui.request_user_letter(entered_letters)
            entered_letters.append(input_letter)
            guessed_word = words.make_masked_word(word, entered_letters)

            if input_letter not in word:
                if attempts_count == attempts:
                    break

                attempts_count += 1

        if word == guessed_word:
            cui.show_win_message()
        elif attempts_count == attempts:
            cui.show_lost_message()

        cui.show_user_statistic(word, guessed_word, entered_letters, attempts_count)

        if cui.request_user_answer().startswith("n"):
            messages.show_goodbye_message()
            break


if __name__ == "__main__":
    game()
