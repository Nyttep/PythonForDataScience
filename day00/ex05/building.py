import sys


def ispunct(c: str) -> bool:
    """ispunct(c: str) -> bool

Check if a character is a punctuation mark\n
Return false if c is not a single character"""
    if (len(c) != 1):
        return False
    return c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def main():
    txt = ""

    if len(sys.argv) > 2:
        sys.exit("AssertionError: More than one argument is provided")

    if len(sys.argv) < 2:
        while len(txt) == 0:
            print("What is the text to count?")
            txt = sys.stdin.readline()
    else:
        txt = sys.argv[1]

    print("The text contains", len(txt), "characters:")
    # could also use sum(1 for c in txt if c.isupper()) but its slower
    # and for me less readable
    print(f"{sum(map(str.isupper, txt))} upper letters")
    print(f"{sum(map(str.islower, txt))} lower letters")
    print(f"{sum(map(ispunct, txt))} punctuation marks")
    print(f"{sum(map(str.isspace, txt))} spaces")
    print(f"{sum(map(str.isdigit, txt))} digits")


if __name__ == '__main__':
    main()
