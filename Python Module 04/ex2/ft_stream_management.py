import sys


def argc_check(argc: int) -> bool:
    if (argc == 1):
        print("please provide arguments ",
              "(python ft_ancient_text.py file.txt)", file=sys.stderr)
        return False
    if (argc != 2):
        print("please only give one file", file=sys.stderr)
        return False
    return True


def read_n_clone(full_lines: list[str]) -> list[str]:
    i = 0
    for line in full_lines:
        new_line = line.replace("\n", "#\n")
        print(line, end="")
        full_lines[i] = new_line
        i += 1
    print("done!")
    print("now cloning...\n")
    for line in full_lines:
        print(line, end="")
    return (full_lines)


def main() -> int:
    argc = len(sys.argv)
    if not argc_check(argc):
        return (1)
    try:
        f = open(sys.argv[1])
    except (PermissionError, FileNotFoundError) as e:
        print(e, file=sys.stderr)
        return (1)

    print("reading...")
    full_lines = f.readlines()
    read_n_clone(full_lines)
    print("\ndone!")
    f.close()
    print("enter file name:(leave empty to ignore): ", end="")
    sys.stdout.flush()
    save_name = sys.stdin.readline().rstrip("\n")
    if save_name == "":
        print("no name was given, deleting file")
        return (0)
    try:
        temp = open(save_name, 'w')
        for line in full_lines:
            temp.write(line)
    except (PermissionError) as e:
        print(e, file=sys.stderr)
        return (0)
    print("file saved as", save_name)
    temp.close()
    return (0)


if __name__ == "__main__":
    _ = main()
