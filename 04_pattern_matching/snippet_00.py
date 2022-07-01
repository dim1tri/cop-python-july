from functools import singledispatch


@singledispatch
def hi_stuart(arg):
    print(f"Hi {arg}")


@hi_stuart.register
def _(arg: str):
    smile = "😊"
    print(f"Hi {arg} {smile}")


@hi_stuart.register
def _(arg: int):
    tripple = arg * 3
    print(f"Hi tripple {tripple}")


hi_stuart(1)
hi_stuart("Bob")
hi_stuart(("str", 42))
