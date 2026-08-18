def input_temperature(temp_str: str) -> int:
    result = 0
    try:
        result = int(temp_str)
    except (TypeError, ValueError):
        print(f"\"{temp_str}\" is not a valid input, please provide"
              "only whole numbers, setting result to 0")
    if result > 40:
        print(f"{result}C is too hot!, please double-check your result. "
              "setting result to 40 which is the max value")
        result = 40
        return result
    if result < 0:
        print(f"{result}C is too cold!, please double-check your result. "
              "setting result to 0 which is the min value")
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

    print("testing 100")
    result = input_temperature("100")
    print(f"temp is {result}C\n")

    print("testing -50")
    result = input_temperature("-50")
    print(f"temp is {result}C\n")


if __name__ == "__main__":
    test_temperature()
    print("End")
