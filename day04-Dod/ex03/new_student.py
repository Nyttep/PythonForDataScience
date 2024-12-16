import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: string
    surname: string
    active: bool = field(default=True)
    login: string = field(default="", init=False)
    id: string = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname.lower()