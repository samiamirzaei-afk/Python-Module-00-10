def input_temperature(temp_str: str) -> int:
    result = int(temp_str)
    if result > 40:
        raise ValueError(f"{result} is larger than 40, use a smaller number")
    if result < 0:
        raise ValueError(f"{result} is smaller than 0, use a smaller number")
    return result


def test_temperature() -> None:
    print("tesing 30")
    test = "30"
    try:
        result = input_temperature(test)
        print(f"temp is {result}C\n")
    except Exception as e:
        print(e)

    print("testing abc")
    test = "abc"
    try:
        result = input_temperature(test)
        print(f"temp is {result}C\n")
    except Exception as e:
        print(e)

    print("testing 100")
    test = "100"
    try:
        result = input_temperature(test)
        print(f"temp is {result}C\n")
    except ValueError as e:
        print(e)

    print("testing 100")
    test = "-50"
    try:
        result = input_temperature(test)
        print(f"temp is {result}C\n")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    test_temperature()
    print("End")
