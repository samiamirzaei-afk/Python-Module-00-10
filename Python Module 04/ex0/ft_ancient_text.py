import sys
# import time


def argc_check(argc: int) -> bool:
    if (argc == 1):
        print("please provide arguments (python ft_ancient_text.py file.txt)")
        return False
    if (argc != 2):
        print("please only give one file")
        return False
    return True


def main() -> int:
    argc = len(sys.argv)
    if not argc_check(argc):
        return (1)
    try:
        f = open(sys.argv[1])
    except (PermissionError, FileNotFoundError) as e:
        print(e)
        return (1)

    print("reading...")
#    time.sleep(1)
    result = f.read()
    print(result)

    print("closing file...")
#    time.sleep(0.6)
    f.close()
    return (0)


if __name__ == "__main__":
    _ = main()
