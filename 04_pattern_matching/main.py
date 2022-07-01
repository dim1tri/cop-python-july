def run_action(user_input: list) -> None:
    if isinstance(user_input, list) and len(user_input) == 2:
        action, value = user_input
        print(f"{action} {value}")
    else:
        print("Wrong command")


run_action("go_right 100".split())
