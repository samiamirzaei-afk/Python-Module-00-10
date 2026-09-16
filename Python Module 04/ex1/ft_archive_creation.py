import sys


def argc_check(argc: int) -> bool:
    if (argc == 1):
        print("please provide arguments (python ft_ancient_text.py file.txt)")
        return False
    if (argc != 2):
        print("please only give one file")
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
    print("\nnow cloning\n\n")
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
        print(e)
        return (1)

    print("reading...")
    full_lines = f.readlines()
    read_n_clone(full_lines)
    print("\n\ndone!")
    f.close()

    save_name = input("enter file name:(leave empty to ignore): ")
    if save_name == "":
        print("no name was given, deleting file")
        return (0)
    try:
        new = open(save_name, 'w')
        for line in full_lines:
            new.write(line)
    except (PermissionError) as e:
        print(e)
        return (1)
    new.close()
    return (0)


if __name__ == "__main__":
    _ = main()
