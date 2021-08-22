from typing import List


def print_menu(menu: List[str]):
    for index, menu_item in enumerate(menu):
        print(f"{index+ 1}. {menu_item}")


def get_input(max_item: int, user_input: str):
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter an integer")
        return
    if 0 < user_input <= max_item:
        return user_input
    print(f"Please enter a number between 1 and {max_item}")
