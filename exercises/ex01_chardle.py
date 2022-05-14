"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730406932"
cinco_character_word: str = input("Enter a 5-character word: ")
if len(cinco_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must be a single character")
        exit()
    else:
        appearances: int = 0
        print("Searching for " + single_character + " in " + cinco_character_word)
        if single_character == cinco_character_word[0]:
            print(single_character + " found at index 0")
            appearances = appearances + 1
        if single_character == cinco_character_word[1]:
            print(single_character + " found at index 1")
            appearances = appearances + 1
        if single_character == cinco_character_word[2]:
            print(single_character + " found at index 2")
            appearances = appearances + 1
        if single_character == cinco_character_word[3]:
            print(single_character + " found at index 3")
            appearances = appearances + 1
        if single_character == cinco_character_word[4]:
            print(single_character + " found at index 4")
            appearances = appearances + 1
        if appearances == 0:
            print("No instances of " + single_character + " found in " + cinco_character_word)
        else:
            if appearances == 1:
                print(str(appearances) + " instance of " + single_character + " found in " + cinco_character_word)
            else:
                print(str(appearances) + " instances of " + single_character + " found in " + cinco_character_word)