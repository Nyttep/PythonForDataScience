class calculator:
    """
    calculator class with basic arithmetic operations

    Attributes:
        vect: list of numbers
    """

    def __init__(self, vect: list) -> None:
        self.vect = vect

    def __add__(self, rhs) -> None:
        print([x + rhs for x in self.vect])

    def __mul__(self, rhs) -> None:
        print([x * rhs for x in self.vect])

    def __sub__(self, rhs) -> None:
        print([x - rhs for x in self.vect])

    def __truediv__(self, rhs) -> None:
        if (rhs == 0):
            print("Error: division by zero is impossible")
        else:
            print([x / rhs for x in self.vect])
