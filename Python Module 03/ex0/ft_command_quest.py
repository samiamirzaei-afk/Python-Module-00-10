import sys

def main() -> int:

    i = 1
    argc = len(sys.argv)
    if argc < 2:
        print("please provice at least one argument")
        return (1)
    while i < argc:
        print(f"argument {i}:", sys.argv[i])
        i += 1

    print(f"total argc: {argc}")
    

if __name__ == "__main__":
    _ = main()

