"""an example of conditional if-else statements"""
SECRET: int = 3
print("i'm thinking of a number between 1-5, what is it?")
guess: int = int(input("what is your guess?"))
if guess == SECRET:
    print("you guessed correctly! have a wonderful day.")
else:
    print("sorry you lose >:) try again.")
print("game over.")