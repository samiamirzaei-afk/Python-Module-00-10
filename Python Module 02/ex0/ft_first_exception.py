def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("tesing 30")
    test = "30"
    try:
        result = input_temperature(test)
        print(f"temp is {result}C\n")
    except (TypeError, ValueError):
        print(f"\"{test}\" is not a valid input "
              "please only give whole numbers, setting value to 0")

    print("testing abc")
    test = "abc"
    try:
        result = input_temperature(test)
        print(f"temp is {result}C\n")
    except (TypeError, ValueError):
        print(f"\"{test}\" is not a valid input "
              "please only give whole numbers, setting value to 0")


if __name__ == "__main__":
    test_temperature()
    print("*** End of program ***")
