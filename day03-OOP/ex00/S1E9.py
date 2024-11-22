from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for a character

Attributes:
    first_name (str): The first name of the character
    is_alive (bool): The status of the character

Methods:
    die: Kill the character"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Class for the Stark family, herits from the Character class

Attributes:
    first_name (str): The first name of the character
    is_alive (bool): The status of the character

Methods:
    die: Kill the character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for the Stark class

Args:
    first_name (str): The first name of the character
Optional args:
    is_alive (bool): Define if the character is alive, default is True"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the character

Sets the is_alive attribute to False"""
        self.is_alive = False
