"""Polishing off Wordle."""
__author__= "730319038"


def contains_char(w: str, l: str) -> bool:
    """Searches the first word for any characters that match the second character."""
    assert len(l) == 1
    i: int = 0
    word: bool = False
    while i < len(w):
        if l == w[i]:
            word = True
            return word
        else:
            i += 1
    return False


def emojified(g: str, s: str) -> str:
    """Color codes letters that match between the two words."""
    assert len(g) == len(s)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji_result: str = ""
    while i < len(g):
        if g[i] == s[i]:
            emoji_result += GREEN_BOX
        else:
            if contains_char(s,g[i]) == True:
                emoji_result += YELLOW_BOX
            else:
                emoji_result += WHITE_BOX
        i += 1
    return(str(emoji_result))


def input_guess(e_g: int) -> str:
    """Asks for a five letter word for you to enter."""
    answer: str = input("Enter a " + str(e_g) + " character word.")
    while e_g != len(answer):
        answer = input("That wasn't " + str(e_g) + " chars! Try again: ")
    return answer


def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    secret: str = "codes"
    winner: bool = True
    while i < 7 and winner:
        print("=== Turn " + str(i) + "/6 ===")
        solution: str = input_guess(len(secret))
        print(emojified(solution, secret))
        if solution == secret:
            print("You won in " + str(i) + " /6 turns!")
            winner = False
        if i == 6:
            print("X/6 - Sorry, try again tomorrow!")
        i += 1

if __name__ == "__main__":
    main()