def garden_operations(operation: int) -> None:
    match operation:
        case 0:
            _ = int("sixseven")
        case 1:
            _ = 10 / 0
        case 2:
            _ = open("/dev/sixseven")
        case 3:
            _ = "hello" + 3
        case _:
            return


def test_error_numbers() -> None:

    try:
        garden_operations(0)
    except ValueError as e:
        print(f"{e}\n")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"{e}\n")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"{e}\n")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"{e}\n")
    garden_operations(67)

    try:
        garden_operations(3)
        garden_operations(2)
        garden_operations(1)
    except (ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"{e}\n")


if __name__ == "__main__":
    test_error_numbers()
    print("End")
