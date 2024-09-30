import os
import words
import state


ATTEMPTS = len(state.HANGMAN_STATE)
WORDS_FILE_NAME = "nounlist.txt"


def show_welcome_message() -> None:
    msg = f"""Welcome to hangman game!
You must guess all letters in random word. Attemt count is {ATTEMPTS}.
The game lasts until you guess the word or until there are attempts left.
"""

    print(msg)


def show_game_status(
    attempt_count: int, player_word: str, guessed_letters: list[str]
) -> None:
    print(
        f"""\nAttempt №{attempt_count}
Your word is => {player_word}
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
                print(f"{validator_error}")
        except Exception as e:
            print(f"{parser_error}: {e}")


def request_user_name():
    return get_user_input(
        "Enter user name",
        lambda input_line: input_line,
        lambda parsed_input: len(parsed_input) > 3 and parsed_input.isalpha(),
        "Enter a valid user name",
        "The name must be longer than 3 char and contain alphabetic characters",
    )


def request_user_letter(guessed_letters: list[str]):
    return get_user_input(
        "Enter your letter",
        lambda input_line: input_line[0],
        lambda parsed_input: parsed_input.isalpha()
        and parsed_input not in guessed_letters,
        "Enter one symbol, please",
        "The letter must be a alphabetic letter and must not have been entered before",
    )


def get_guessed_letters(target_word: str, entered_letters: list[str]) -> list[str]:
    return [ch for ch in target_word if ch in entered_letters]


def show_user_statistic(
    attempt_count: int, entered_letters: list[str], target_word: str, user_word: str
):
    guessed_letters = get_guessed_letters(target_word, entered_letters)
    placeholder = "-" * (35 + len(entered_letters * 3))

    print(
        f"""
Your statictics:
{placeholder}
| The guess word was =>         {target_word}
| The number of attempts was => {attempt_count}
| Entered letters =>            {", ".join(entered_letters)}
| Your word =>                  {user_word}
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
        target_word = words.get_random_word(filepath)
        entered_letters = []
        guessed_word = words.make_masked_word(target_word, entered_letters)
        attempt_count = 1

        while guessed_word != target_word and attempt_count <= ATTEMPTS:
            show_game_status(attempt_count, guessed_word, entered_letters)

            input_letter = request_user_letter(entered_letters)
            entered_letters.append(input_letter)
            guessed_word = words.make_masked_word(target_word, entered_letters)

            if input_letter not in target_word:
                if attempt_count == ATTEMPTS:
                    break

                attempt_count += 1

        if target_word == guessed_word:
            print("\nYou won the game! Congratulation! :)")
        elif attempt_count == ATTEMPTS:
            print("\nYou lost by running out of tries. :(")

        show_user_statistic(attempt_count, entered_letters, target_word, guessed_word)

        if input("Do you want one more game? y/n ").lower()[0] == "n":
            show_goodbye_message()
            break


if __name__ == "__main__":
    game()
