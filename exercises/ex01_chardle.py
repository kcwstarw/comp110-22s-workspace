"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730319038"

help_me: str = input("Enter a 5-character word:")
len(help_me) == 5
if len(help_me) != 5:
    print("Error: Word must contain 5 characters")
    exit()
save_me: str = input("Enter a single character:")
len(save_me) == 1
if len(save_me) != 1:
    print("Error: Character must be a single character")
    exit()
lets_go: int = 0
print("Searching for " + save_me + " in " + help_me)

if save_me == help_me[0]:
    print(save_me + " found at index " + str(0))
    lets_go = lets_go + 1
if save_me == help_me[1]:
    print(save_me + " found at index " + str(1))
    lets_go = lets_go + 1
if save_me == help_me[2]:
    print(save_me + " found at index " + str(2))
    lets_go = lets_go + 1
if save_me == help_me[3]:
    print(save_me + " found at index " + str(3))
    lets_go = lets_go + 1
if save_me == help_me[4]:
    print(save_me + " found at index " + str(4))
    lets_go = lets_go + 1

print(str(lets_go) + " instances of " + str(save_me) + " found in " + str(help_me))