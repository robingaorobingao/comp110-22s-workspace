"""wordle!!!"""
__author__ = "730406932"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(any_length: str, single_character: str) -> bool:
    """Its purpose is when given two strings, the first of any length, the second a single character, it will return True if the single character of the second string is found at any index of the first string, and return False otherwise."""
    assert len(single_character) == 1
    i: int = 0
    # testing to see if the character matches up anywhere in the word
    while i < len(any_length):
        if single_character == any_length[i]:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Its purpose is given two strings of equal length, the first a guess and the second a secret, it will return a string of emoji whose color codifies the same as you previously implemented in EX02."""
    assert len(guess) == len(secret)
    i: int = 0
    emoji: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        # i'm not sure why i don't have to specify "contains_char(secret, guess[i]) is True" here for the bool but... my code works the same as the example inputs provided by the website so i'm gonna keep it like this lol
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(expected: int) -> str:
    """Its purpose is given an integer “expected length” of a guess as a parameter, it will prompt the user for a guess and continue prompting them until they provide a guess of the expected length."""
    enter: str = input(f"Enter a {expected} character word: ")
    while len(enter) != expected:
        enter = input(f"That wasn't {expected} chars! Try again: ")
    return enter


def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    turns: int = 6
    secret_word: str = "codes"
    # running the game!
    while i <= turns:
        print(f"=== Turn {i}/{turns} ===")
        nice_try: str = input_guess(len(secret_word))
        print(emojified(nice_try, secret_word))
        if secret_word == nice_try:
            print(f"You won in {i}/{turns} turns!")
            # i = 7 to stop the game
            i = 7
        elif i == turns:
            print(f"X/{turns} - Sorry, try again tomorrow!")
            i = 7
        else:
            i += 1


if __name__ == "__main__":
    main()