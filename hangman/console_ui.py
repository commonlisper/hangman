import state
from answer import Answer


def request_user_letter(guessed_letters: list[str]) -> str:
    while True:
        user_input = input("Enter your letter: ").lower()

        if len(user_input) > 1:
            print("Enter onle one symbol, please")
            continue

        if not user_input.isascii():
            print("The letter must be in Latin alphabet")
            continue

        if not user_input.isalpha():
            print("The letter must be a alphabetic letter")
            continue

        if user_input in guessed_letters:
            print("The letter must not have been entered before")
            continue

        return user_input


def request_user_answer() -> str:
    while True:
        user_input = input("Do you want one more game? y/n ").lower()

        if len(user_input) > 1:
            print("Enter onle one symbol, please")
            continue

        if not user_input.isascii():
            print("The letter must be in Latin alphabet")
            continue

        if not user_input.isalpha():
            print("The letter must be a alphabetic letter")
            continue

        if user_input not in (Answer.YES.value, Answer.NO.value):
            print("The letter must be in `y` or `n`")
            continue

        return user_input


def show_game_status(attempt_count: int, guessed_word: str, guessed_letters: list[str]) -> None:
    print(f"\nAttempt №{attempt_count}")
    print(f"Your word is => {guessed_word}")
    print(f"Letters you've guessed => {guessed_letters}")
    print(f"{state.HANGMAN_STATE[attempt_count - 1]}\n")


def _get_guessed_letters(target_word: str, entered_letters: list[str]) -> list[str]:
    return [ch for ch in target_word if ch in entered_letters]


def show_user_statistic(
    word: str,
    guessed_word: str,
    entered_letters: list[str],
    attempts_count,
):
    guessed_letters = _get_guessed_letters(word, entered_letters)
    placeholder = "-" * (35 + len(entered_letters * 3))

    print("Your statictics:")
    print(placeholder)
    print(f"| The guess word was =>         {word}")
    print(f"| The number of attempts was => {attempts_count}")
    print(f"| Entered letters =>            {", ".join(entered_letters)}")
    print(f"| Your word =>                  {guessed_word}")
    print(f"| Guessed letters =>            {", ".join(guessed_letters)}")
    print(placeholder)


def show_win_message() -> None:
    print("\nYou won the game! Congratulation! :)\n")


def show_lost_message() -> None:
    print("\nYou lost by running out of tries. :(")
    print(f"{state.HANGMAN_STATE[-1]}\n")


def show_welcome_message(attempts_count: int) -> None:
    print("Welcome to hangman game!")
    print(f"You must guess all letters in random word. Attemt count is {attempts_count}.")
    print("The game lasts until you guess the word or until there are attempts left.")


def show_goodbye_message() -> None:
    print("Thank you for playing our game. Have a good day!")
