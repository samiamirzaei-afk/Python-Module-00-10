import sys


def argc_check(argc: int) -> bool:
    if (argc == 1):
        print("please provide arguments (python ft_ancient_text.py file.txt)")
        return False
    if (argc != 2):
        print("please only give one file")
        return False
    return True


def secure_archive(argv: str, option: int) -> tuple[bool, str]:
    mode = "r" if option == 1 else "w"
    try:
        with open(argv) as f:
            content = f.read()
            if mode == "w":
                with open("archive.txt", mode) as f2:
                    f2.write(content)
                    f2.write("###archive text###")
                    return(True, "content wrote in file \"archive.txt\"")
            return(True, content)
    except (FileNotFoundError, PermissionError) as e:
        return(False, str(e))


def main() -> int:
    read = 1
    write = 2
    argc = len(sys.argv)
    if not argc_check(argc):
        return (1)
    result = secure_archive(sys.argv[1], read)
    print(result)
    result = secure_archive(sys.argv[1], write)
    print(result)
    return (0)


if __name__ == "__main__":
    _ = main()
