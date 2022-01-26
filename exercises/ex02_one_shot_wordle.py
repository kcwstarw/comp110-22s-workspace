"""One Shot Wordle Assignemnt"""
__author__ = "730319038"

secret_word: str = "python"
guess: str = str(input(f"What is your {len(secret_word)}-letter word? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
i: int = 0
ii: int = 0
emoji_result: str = ""
word: bool = False
while i < len(secret_word):
    if guess[i] == secret_word[i]:
        emoji_result += GREEN_BOX
    else: 
        while ii < len(secret_word):
            if guess[i] == secret_word[ii]:
                word = True
            ii = ii + 1
        if word == True:
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
    i = i + 1
print(emoji_result)
if len(guess) == len(secret_word) and guess != secret_word:
    print("Not quite. Play again soon!")







if guess == secret_word:
    print("Woo! You got it!")