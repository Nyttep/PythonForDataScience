class calculator:
    """
    calculator class
    contains methods to perform dot product, add and substract vectors
    """

    def __init__(self):
        pass

    @classmethod
    def dotproduct(self, lhs: list[float], rhs: list[float]) -> None:
        """
        Dot product of two vectors
        """
        res: float = sum([x * y for (x, y) in zip(lhs, rhs)])
        print(f"Dot product is: {res}")

    @classmethod
    def add_vec(self, lhs: list[float], rhs: list[float]) -> None:
        """
        Add two vectors
        """
        res: list[float] = [x + y for (x, y) in zip(lhs, rhs)]
        print(f"Add Vector is: {res}")

    @classmethod
    def sous_vec(self, lhs: list[float], rhs: list[float]) -> None:
        """
        Substract two vectors
        """
        res: list[float] = [x - y for (x, y) in zip(lhs, rhs)]
        print(f"Sous Vector is: {res}")
