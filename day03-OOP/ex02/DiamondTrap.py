from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class for the King family, inherits from Baratheon and Lannister classes.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The status of the character.

    Methods:
        die: Kill the character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the King class.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Define if the character is alive.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """
        Set the eyes color of the character.

        Args:
            eyes (str): The eyes color of the character.
        """
        self.eyes = eyes

    def get_eyes(self) -> str:
        """
        Get the eyes color of the character.

        Returns:
            str: The eyes color of the character.
        """
        return self.eyes

    def set_hairs(self, hairs: str):
        """
        Set the hairs color of the character.

        Args:
            hairs (str): The hairs color of the character.
        """
        self.hairs = hairs

    def get_hairs(self) -> str:
        """
        Get the hairs color of the character.

        Returns:
            str: The hairs color of the character.
        """
        return self.hairs
