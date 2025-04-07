"""Implement a main function that contains the main loop of the Wordle game."""

__author__ = "730734417"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:  # type: ignore
    """Checks to see if character is included in the player's given string"""
    assert len(char) == 1, f"len{'(char)'} is not 1"

    i: int = 0

    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns an emoji string to indicate correctness of guesses"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    emojis: str = ""
    i: int = 0

    while i < len(guess):
        if guess[i] == secret[i]:
            emojis += GREEN_BOX
        elif contains_char(guess, secret[i]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis


def input_guess(guess_len: int) -> str:
    """Collects a guess of the desired length from the user"""
    guess: str = input(f"Enter a {guess_len} character word: ")

    while len(guess) != guess_len:
        guess = input(f"That wasn't {guess_len} chars! Try again: ")

    return guess


def main(game_secret: str) -> None:
    """Main game loop"""
    turn: int = 1
    guessed: bool = False
    player_guess: str = ""

    while not guessed and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        player_guess = input_guess(len(game_secret))

        print(emojified(player_guess, game_secret))

        if player_guess == game_secret:
            guessed = True
        else:
            turn += 1

    if guessed:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(game_secret="codes")
