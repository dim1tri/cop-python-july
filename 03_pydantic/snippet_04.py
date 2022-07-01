from typing import List
from pydantic import BaseModel, validator
from pydantic import parse_raw_as


class Bro(BaseModel):
    name: str
    age: int

    @validator("age")
    def real_age(cls, age):
        assert age > 0 and age < 100
        return age


with open("bros.json") as bro_file:
    bros = parse_raw_as(List[Bro], bro_file.read())

print(bros)
