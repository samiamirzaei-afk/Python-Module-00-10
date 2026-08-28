import math


def parse(raw: str) -> tuple[bool, float, float, float]:
    i = 0
    try:
        x, y, z = raw.split(",")
    except ValueError:
        print("Invalid syntax, example of a valid syntax: <5, -10, 20.4,>")
        return (False, 1, 1, 1)
    try:
        x = float(x)
        y = float(y)
        z = float(z)
    except ValueError:
        return (False, 1, 1, 1)
    return (True, x, y, z)


def main() -> int:
    print("=== Game Coordinate System ===")
    raw = input("Enter Player one's x, y, z coordinates please: ")
    result, x, y, z = parse(raw)
    while 1:
        if result is True:
            break
        raw = input("Enter Player one's x, y, z coordinates please: ")
        result, x, y, z = parse(raw)
    print(f"Coordinates of Player one:({x=}, {y=}, {z=})")
    math_result = math.sqrt((x-0)**2 +(y-0)**2 + (z-0)**2)
    print(f"Player one's distance from the center: {round(math_result, 2)}")
    
    raw1 = input("Enter Player two's x, y, z coordinates please: ")
    result, x1, y1, z1 = parse(raw1)
    while 1:
        if result is True:
            break
        raw1 = input("Enter Player two's x, y, z coordinates please: ")
        result, x1, y1, z1 = parse(raw1)
    print(f"Coordinates of Player one:({x1=}, {y1=}, {z1=})")
    math_result = math.sqrt((x-x1)**2 +(y-y1)**2 + (z-z1)**2)
    print(f"Player two's distance from Plater one: {round(math_result, 2)}")

if __name__ == "__main__":
    _ = main()
