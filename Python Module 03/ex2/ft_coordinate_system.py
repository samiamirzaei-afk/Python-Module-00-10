import math

def parse(raw: str) -> tuple[bool, float, float, float]:
    try:
        x, y, z = raw.split(",")
    except ValueError:
        print("invalid syntax, example of correct syntax: <1, 3, 4>")
        return(False, 0, 0, 0)
    try:
        x = float(x)
        y = float(y)
        z = float(z)
    except ValueError:
        print("invalid syntax, example of correct syntax: <1, 3, 4>")
        return(False, 0, 0, 0)
    return(True, x, y, z)
def main() -> int:
    while(1):
        raw = input("please give x, y, z: ")
        result, x, y, z = parse(raw)
        if(result is True):
            break
    print(f"first set: {x=}, {y=}, {z=}")

    center_dis = math.sqrt((x-0)**2 + (y-0)**2 + (z-0)**2)
    print("distance to center %.2f" % (center_dis))

    while(1):
        raw = input("second player's x, y, z: ")
        result, x1, y1, z1 = parse(raw)
        if(result is True):
            break
    print(f"second player: {x=}, {y=}, {z=}")

    center_dis = math.sqrt((x1-x)**2 + (y1-y)**2 + (z1-z)**2)
    print("distance to firstplayer %.2f" % (center_dis))

if __name__ == "__main__":
    _ = main()
