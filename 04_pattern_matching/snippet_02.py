def run_action(user_input: list) -> None:
    match user_input:
        case "shoot", target:
            print(f"Shooting {target}")
        case action, value:
            print(f"{action} {value}")
        case action, value, extra_value:
            print(f"{action} {value} extra: {extra_value}")
        case _:
            print("Wrong command")


run_action("go_right 100".split())
run_action("go_left 100 1".split())
run_action("shoot tower".split())
