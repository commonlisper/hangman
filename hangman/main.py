import os
import words
import state
from ValidationException import ValidationException

ATTEMPTS = len(state.HANGMAN_STATE)
WORDS_FILE_NAME = "nounlist.txt"


def show_welcome_message() -> None:
    msg = f"""Welcome to hangman game!
You must guess all letters in random word. Attemt count is {ATTEMPTS}.
The game lasts until you guess the word or until there are attempts left.
"""

    print(msg)


def show_game_status(
    attempt_count: int, guessed_word: str, guessed_letters: list[str]
) -> None:
    print(
        f"""\nAttempt №{attempt_count}
Your word is => {guessed_word}
Letters you've guessed => {guessed_letters}

{state.HANGMAN_STATE[attempt_count - 1]}\n"""
    )


def get_user_input(msg, parser, is_valid, parser_error, validator_error) -> str:
    while True:
        user_input = input(f"{msg}: ")

        try:
            parsed_input = parser(user_input)

            if is_valid(parsed_input):
                return parsed_input
            else:
                raise ValidationException(f"{validator_error}")
        except ValidationException as ex:
            print(f"{ex}")
        except Exception:
            print(f"{parser_error}")


def request_user_letter(guessed_letters: list[str]):
    return get_user_input(
        "Enter your letter",
        lambda input_line: input_line[0],
        lambda parsed_input: parsed_input.isalpha()
        and parsed_input not in guessed_letters,
        "Enter one symbol, please",
        "The letter must be a alphabetic letter and must not have been entered before",
    )


def request_user_answer():
    return get_user_input(
        "Do you want one more game? y/n ",
        lambda input_line: input_line[0],
        lambda parsed_input: parsed_input.isalpha() and parsed_input in ("y", "n"),
        "Enter only one symbol",
        "The symbol must be in `y` or `n`",
    )


def get_guessed_letters(target_word: str, entered_letters: list[str]) -> list[str]:
    return [ch for ch in target_word if ch in entered_letters]


def show_user_statistic(
    word: str,
    guessed_word: str,
    entered_letters: list[str],
    attempts_count,
):
    guessed_letters = get_guessed_letters(word, entered_letters)
    placeholder = "-" * (35 + len(entered_letters * 3))

    print(
        f"""
Your statictics:
{placeholder}
| The guess word was =>         {word}
| The number of attempts was => {attempts_count}
| Entered letters =>            {", ".join(entered_letters)}
| Your word =>                  {guessed_word}
| Guessed letters =>            {", ".join(guessed_letters)}
{placeholder}
"""
    )


def show_goodbye_message():
    print("Thank you for playing our game. Have a good day!")


def game():
    show_welcome_message()
    while True:
        filepath = f"{os.getcwd()}{os.sep}{WORDS_FILE_NAME}"
        word = words.get_random_word(filepath)
        entered_letters = []
        guessed_word = words.make_masked_word(word, entered_letters)
        attempts_count = 1

        while guessed_word != word and attempts_count <= ATTEMPTS:
            show_game_status(attempts_count, guessed_word, entered_letters)

            input_letter = request_user_letter(entered_letters)
            entered_letters.append(input_letter)
            guessed_word = words.make_masked_word(word, entered_letters)

            if input_letter not in word:
                if attempts_count == ATTEMPTS:
                    break

                attempts_count += 1

        if word == guessed_word:
            print("\nYou won the game! Congratulation! :)")
        elif attempts_count == ATTEMPTS:
            print("\nYou lost by running out of tries. :(")

        show_user_statistic(word, guessed_word, entered_letters, attempts_count)

        if request_user_answer().startswith("n"):
            show_goodbye_message()
            break


if __name__ == "__main__":
    game()
