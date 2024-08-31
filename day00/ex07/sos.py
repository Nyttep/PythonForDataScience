import sys


def check_args(argv: list):
    """check_args(argv: list) -> bool

Check if the arguments are valid\n
Return False if the arguments are bad\n
Return True if the arguments are good"""

    if len(argv) != 2:  # check  if there is only 1 arg
        return False

    # check if the first argument is a valid string
    if all([str.isalnum(c) or str.isspace(c) for c in argv[1]]) is False:
        return False

    return True


def main():
    if check_args(sys.argv) is False:
        sys.exit("AssertionError: the arguments are bad")

    MORSE_DICT = {" ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ",
                  "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ",
                  "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
                  "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
                  "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
                  "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
                  "X": "-..- ", "Y": "-.-- ", "Z": "--.. ", "0": "----- ",
                  "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
                  "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ",
                  "9": "----. "}
    # convert string to uppercase + transform multiple spaces into one
    txt = " ".join(sys.argv[1].upper().split())
    morse = txt.translate(str.maketrans(MORSE_DICT))
    print(morse)


if __name__ == '__main__':
    main()
