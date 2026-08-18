def input_temperature(temp_str: str) -> int:
    result = 0
    try:
        result = int(temp_str)
    except (ValueError, TypeError):
        print(f"\"{temp_str}\" is not a valid input "
              "please only give whole numbers, setting value to 0")
    return result


def test_temperature() -> None:
    print("tesing 30")
    result = input_temperature("30")
    print(f"temp is {result}C\n")

    print("testing mnba")
    result = input_temperature("mnba")
    print(f"temp is {result}C\n")

    print("testing 1.3")
    result = input_temperature("1.3")
    print(f"temp is {result}C\n")


if __name__ == "__main__":
    test_temperature()
    print("End")
