import sys as sys

if len(sys.argv) > 2:
    sys.exit("AssertionError: more than one argument is provided")
if len(sys.argv) < 2:
    sys.exit(0)

try:
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    sys.exit("AssertionError: argument is not an integer")
