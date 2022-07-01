def run_action(user_input: list) -> None:
    match user_input:
        case action, value:
            print(f"{action} {value}")
        case _:
            print("Wrong command")


run_action("go_right 100".split())
