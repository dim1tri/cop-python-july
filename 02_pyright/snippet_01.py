def hello(bro: str) -> str:
    return f"Hello {bro}"


def calculate_age(bro: str) -> int:
    return 42


def happy_birthday(bro: str) -> str:
    greeting = hello(bro) + calculate_age(42)
