from typing import Union


def hello(bro: Union[str, int]) -> None:
    if isinstance(bro, str):
        print("Hello " + bro)
    if isinstance(bro, int):
        if bro > 42:
            print("Hello Alice")
        else:
            print("Hello Bob")


hello("Bob")
hello(42)
