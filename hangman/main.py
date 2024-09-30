import os
import words
import pics

ATTEMPTS = len(pics.HANGMAN_STATE)
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

{pics.HANGMAN_STATE[attempt_count - 1]}\n"""
    )


def get_user_input(guessed_chars: list[str]) -> str:
    while True:
        input_char = input("Please, enter the character: ")[0]

        if not input_char.isalpha():
            print("Enter a character, not something else")
            continue

        if input_char in guessed_chars:
            print("That's the symbol you've already guessed, try another.")
            continue

        return input_char


def get_guessed_chars(random_word: str, entered_chars: list[str]) -> list[str]:
    guessed_chars = [ch for ch in random_word if ch in entered_chars]
    return guessed_chars


def show_user_statistic(
    attempt_count: int, entered_chars: list[str], player_word: str, random_word: str
):
    guessed_chars = get_guessed_chars(random_word, entered_chars)
    placeholder = "-" * (35 + len(entered_chars * 3))

    print(
        f"""
Your statictics:
{placeholder}
| The guess word was =>         {random_word}
| The number of attempts was => {attempt_count}
| Entered letters =>            {", ".join(entered_chars)}
| Your word =>                  {player_word}
| Guessed letters =>            {", ".join(guessed_chars)}
{placeholder}
"""
    )


def show_goodbye_message():
    print("Thank you for playing our game. Have a good day!")


def game():
    show_welcome_message()
    while True:
        target_word = words.get_random_word(f"{os.getcwd()}{os.sep}{WORDS_FILE_NAME}")
        entered_chars = []
        guessed_word = words.get_masked_word(target_word, entered_chars)
        attempt_count = 1

        while guessed_word != target_word and attempt_count <= ATTEMPTS:
            show_game_status(attempt_count, guessed_word, entered_chars)

            input_char = get_user_input(entered_chars)
            entered_chars.append(input_char)
            guessed_word = words.get_masked_word(target_word, entered_chars)

            if input_char not in target_word:
                if attempt_count == ATTEMPTS:
                    break

                attempt_count += 1

        if target_word == guessed_word:
            print("\nYou won the game! Congratulation! :)")
        elif attempt_count == ATTEMPTS:
            print("\nYou lost by running out of tries. :(")

        show_user_statistic(attempt_count, entered_chars, guessed_word, target_word)

        if input("Do you want one more game? y/n").lower()[0] == "n":
            show_goodbye_message()
            break


if __name__ == "__main__":
    game()
