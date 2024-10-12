def show_welcome_message(attempts_count: int) -> None:
    msg = f"""Welcome to hangman game!
You must guess all letters in random word. Attemt count is {attempts_count}.
The game lasts until you guess the word or until there are attempts left.
"""

    print(msg)


def show_goodbye_message() -> None:
    print("Thank you for playing our game. Have a good day!")
