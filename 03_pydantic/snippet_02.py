from pydantic import BaseModel, validator


class Bro(BaseModel):
    name: str
    age: int

    @validator("age")
    def real_age(cls, age):
        assert age > 0 and age < 100
        return age


bro = Bro(name="Bob", age=42)
print(bro.dict())
