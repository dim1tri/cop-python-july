from pydantic import BaseModel


class Bro(BaseModel):
    name: str
    age: int


bro = Bro(name="Alice", age=42)

match bro:
    case Bro(name="Alice" | "Bob", age=bro_age) if bro_age > 42:
        print(f"Bro is adult")
    case Bro():
        print("Bro is bro")
