from typing import Callable
from ValidationException import ValidationException
import state


def _get_user_input(
    input_message: str,
    parser: Callable[[str], str],
    is_valid: Callable[[str], bool],
    parser_error: str,
    validator_error: str,
) -> str:
    while True:
        user_input = input(f"{input_message}: ")

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


def request_user_letter(guessed_letters: list[str]) -> str:
    return _get_user_input(
        "Enter your letter",
        lambda input_line: input_line[0],
        lambda parsed_input: parsed_input.isalpha()
        and parsed_input not in guessed_letters,
        "Enter one symbol, please",
        "The letter must be a alphabetic letter and must not have been entered before",
    )


def request_user_answer() -> str:
    return _get_user_input(
        "Do you want one more game? y/n ",
        lambda input_line: input_line[0],
        lambda parsed_input: parsed_input.isalpha() and parsed_input in ("y", "n"),
        "Enter only one symbol",
        "The symbol must be in `y` or `n`",
    )


def show_game_status(
    attempt_count: int, guessed_word: str, guessed_letters: list[str]
) -> None:
    print(
        f"""\nAttempt №{attempt_count}
Your word is => {guessed_word}
Letters you've guessed => {guessed_letters}

{state.HANGMAN_STATE[attempt_count - 1]}\n"""
    )


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
