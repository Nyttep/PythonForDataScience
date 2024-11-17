from S1E9 import Character


class Baratheon(Character):
    """Class for the Baratheon family, herits from the Character class

Attributes:
    first_name (str): The first name of the character
    is_alive (bool): The status of the character

Methods:
    die: Kill the character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for the Baratheon class

Args:
    first_name (str): The first name of the character
Optional args:
    is_alive (bool): Define if the character is alive, default is True"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the character"""
        self.is_alive = False


class Lannister(Character):
    """Class for the Lannister family, herits from the Character class

Attributes:
    first_name (str): The first name of the character
    is_alive (bool): The status of the character

Methods:
    die: Kill the character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for the Lannister class

Args:
    first_name (str): The first name of the character
Optional args:
    is_alive (bool): Define if the character is alive, default is True"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the character"""
        self.is_alive = False
