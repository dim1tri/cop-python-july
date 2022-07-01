import json
from dataclasses import dataclass


@dataclass
class Bro:
    name: str
    age: int


with open("bro.json") as bro_file:
    data = json.load(bro_file)
    bro = Bro(**data)

print(bro)
