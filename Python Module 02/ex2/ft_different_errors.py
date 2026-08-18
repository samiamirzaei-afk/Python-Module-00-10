def mama(oida: int) -> None:
    match oida:
        case 0:
            _ = int("sixseven")
        case 1:
            _ = 10 / 0
        case 2:
            _ = open("/dev/urmum")
        case 3:
            _ = "hello" + 3
        case _:
            raise SystemExit("i am the gooner of gooners i am samy deez nuts")


if __name__ == "__main__":
    try:
        mama(0)
    except ValueError as e:
        print(e)
    try:
        mama(1)
    except ZeroDivisionError as e:
        print(e)
    try:
        mama(2)
    except FileNotFoundError as e:
        print(e)
    try:
        mama(3)
    except TypeError as e:
        print(e)
    mama(67)
    print("End")
