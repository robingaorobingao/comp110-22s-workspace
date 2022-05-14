"""examples of using lists in a simple 'game'."""
from random import randint
rolls: list[int] = list()  # empty list with nothing in it
while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))
print(rolls)
rolls.pop(len(rolls) - 1)  # remove the last item from a list
print(rolls)
i: int = 0  # sum of vallues of our rolls
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1
print(f"Total score: {sum}")
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)
# print(rolls[3])  # access individual item
# print(rolls[1])
# print(len(rolls))  # access length of list
# print(rolls[len(rolls) - 1])  # access last item of list