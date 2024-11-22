from S1E9 import Character


class Baratheon(Character):
    """
    Class for the Baratheon family, herits from the Character class

    Attributes:
        first_name (str): The first name of the character
        is_alive (bool): The status of the character

    Methods:
        die: Kill the character
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Baratheon class

        Args:
            first_name (str): The first name of the character

        Optional args:
            is_alive (bool): Define if the character is alive, default is True"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        ret: str = "Vector: "
        ret += f"('{type(self).__name__}', '{self.eyes}', '{self.hairs}')"
        return ret

    def __repr__(self) -> str:
        ret: str = "Vector: "
        ret += f"('{type(self).__name__}', '{self.eyes}', '{self.hairs}')"
        return ret

    def die(self):
        """
        Kill the character
        """
        self.is_alive = False


class Lannister(Character):
    """
    Class for the Lannister family, inherits from the Character class.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The status of the character.

    Methods:
        die: Kill the character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Lannister class.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Define if the character is alive, default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """
        String representation of the Lannister object.

        Returns:
            str: A string describing the Lannister object.
        """
        return f"Vector: ('{type(self).__name__}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Official string representation of the Lannister object.

        Returns:
            str: A string describing the Lannister object.
        """
        return f"Vector: ('{type(self).__name__}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Kill the character.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Creates another Lannister object

        You can call it either directly from the class
        (e.g. Lannister.create_lannister(first_name, is_alive))
        or from an instance of the class
        (e.g. Lannister().create_lannister(first_name, is_alive))
        """
        return cls(first_name, is_alive)
