from ft_filter import ft_filter
import sys


def ispunct(c: str) -> bool:
    """ispunct(c: str) -> bool

Check if a character is a punctuation mark\n
Return false if c is not a single character"""

    if (len(c) != 1):
        return False
    return c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def argsCheck(argv: list) -> bool:
    """argsCheck(argv: list) -> bool

Check if the arguments are valid\n
Return False if the arguments are bad\n
Return True if the arguments are good"""

    if len(argv) != 3:  # check if there is 2 args
        return False

    try:  # check if the second argument is a positive integer
        if int(argv[2]) < 0:
            return False
    except ValueError:
        return False

    # check if the first argument is a valid string
    # (no punctuation or invisible char)
    if all([not ispunct(c) and str.isprintable(c) for c in argv[1]]) is False:
        return False

    return True


def main():
    if argsCheck(sys.argv) is False:
        sys.exit("AssertionError: the arguments are bad")
    txt = sys.argv[1]
    n = int(sys.argv[2])
    print(list(ft_filter(lambda word: len(word) > n, txt.split())))


if __name__ == '__main__':
    main()
