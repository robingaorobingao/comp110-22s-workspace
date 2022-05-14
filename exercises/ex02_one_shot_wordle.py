"""one shot wordle!"""
__author__ = "730406932"
i: int = 0
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "python"
length: int = len(secret)
guess: str = str(input(f"What is your {length}-letter guess? "))
while len(guess) != length:
    guess = str(input(f"That was not {length} letters! Try again: "))
while i < length:
    exist: bool = False
    if guess[i] == secret[i]:
        emoji += GREEN_BOX
    elif guess[i] != secret[i]:
        idx: int = 0
        while exist is False and idx < length:
            if guess[i] == secret[idx]:
                exist = True
            else:
                idx += 1
        if exist is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i += 1
print(emoji)
if secret == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")