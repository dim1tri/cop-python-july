from dataclasses import dataclass


@dataclass
class Bro:
    name: str
    age: int


bro = Bro(name="Bob", age=42)
print(bro)
