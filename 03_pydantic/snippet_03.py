import json
from pydantic import BaseModel, validator


class Bro(BaseModel):
    name: str
    age: int

    @validator("age")
    def real_age(cls, age):
        assert age > 0 and age < 100
        return age


with open("bro.json") as bro_file:
    data = json.load(bro_file)
    bro = Bro(**data)

print(bro)
