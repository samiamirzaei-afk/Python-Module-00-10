import math


def parse(raw: str) -> tuple[bool, float, float, float]:
    try:
        x, y, z = raw.split(",")
    except ValueError:
        print("Invalid syntax, example of a valid syntax: <5, -10, 20.4,>")
        return (False, 1, 1, 1)
    try:
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
    except ValueError:
        return (False, 1, 1, 1)
    return (True, x1, y1, z1)


def main() -> int:
    print("=== Game Coordinate System ===")
    while 1:
        raw = input("Enter Player one's x, y, z coordinates please: ")
        result, x, y, z = parse(raw)
        if result is True:
            break
    print(f"Coordinates of Player one:({x=}, {y=}, {z=})")
    math_result = math.sqrt((x-0)**2 + (y-0)**2 + (z-0)**2)
    print(f"Player one's distance from the center: {round(math_result, 2)}")

    while 1:
        raw1 = input("Enter Player two's x, y, z coordinates please: ")
        result, x2, y2, z2 = parse(raw1)
        if result is True:
            break
    print(f"Coordinates of Player one:({x2=}, {y2=}, {z2=})")
    math_result = math.sqrt((x2-x)**2 + (y2-y)**2 + (z2-z)**2)
    print(f"Player two's distance from Plater one: {round(math_result, 2)}")
    return (0)


if __name__ == "__main__":
    _ = main()
