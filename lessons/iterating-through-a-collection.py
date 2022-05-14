"""example of looping through all characters in a string"""
user: str = input("Gimme a string! ")
# variable i is a common counter variable name in programming
i: int = 0
while 1 < len(user):
    print(user[i])
    i = i + 1
print("Done!")