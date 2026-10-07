import sys
import platform


def main() -> int:
    vm = sys.prefix != sys.base_prefix
    print("prefix:          ", sys.prefix)
    print("base_prefix:     ", sys.base_prefix)
    print("exec_prefix:     ", sys.exec_prefix)
    print("base_exec_prefix:", sys.base_exec_prefix)
    print("sys.version      ", sys.version)
    print()
    print("sys.version_info ", sys.version_info)
    print("platform.python_version", platform.python_version())
    print("sys.executable   ", sys.executable)
    print("in venv:         ", vm)
    if vm:
        print("\nyou are in a virtual environment")
        print('to exit, type "deactivate"')
    else:
        print("\nyou are not in a virtual enviroment")
        print('to make one, type " python3 -m venv FILE_NAME"')
        print('to enter, type " source FILE_NAME/bin/activate"')

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
