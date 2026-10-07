import sys
import importlib


ModuleType = type(sys)


def help_message(missing: list[str]) -> None:
    full_name = ""
    print("\nimport the missing Module:")
    print("if you are using pip, Do:")
    for name in missing:
        full_name += name + " "
    print(f"pip install {full_name}")
    print('or simply do "pip install -r requirements.txt"')
    print("\nif you are using poetry, Do:")
    print(f"poetry add {full_name}")
    print('or simply do "poetry install"')
    print("\nsimply rerun the program after installing the needed files")


def dep_check(name: str) -> tuple[bool, str, ModuleType | None]:
    try:
        result = importlib.import_module(name)
    except (ModuleNotFoundError, ImportError):
        return (False, name, None)
    return (True, name, result)


def status_check(result: list[tuple[bool, str, ModuleType | None]]) -> bool:
    is_fail = False
    missing = []
    for pack in result:
        stat, name, lib = pack

        if stat is False:
            is_fail = True
            print(name, "was not imported")
            missing.append(name)
            continue
        print(name, "passed")
    if is_fail is True:
        help_message(missing)
    print("starting program...\n\n")
    return is_fail


def ft_run_impoter() -> list[ModuleType]:
    result = list()
    result.append(dep_check("numpy"))
    result.append(dep_check("pandas"))
    result.append(dep_check("matplotlib.pyplot"))
    result.append(dep_check("requests"))
    print("*Over all statis:*\n")
    if status_check(result):
        print("exiting....")
        sys.exit(1)
    final_result = list()
    for _, _, mod in result:
        final_result.append(mod)
    return final_result


def ft_vm() -> None:
    print("prefix:          ", sys.prefix)
    print("base_prefix:     ", sys.base_prefix)
    print("exec_prefix:     ", sys.exec_prefix)
    print("base_exec_prefix:", sys.base_exec_prefix)
    vm = sys.prefix != sys.base_prefix
    if vm:
        print("\nyou are in a virtual environment")
        if "pypoetry" in sys.prefix:
            print("using Poetry")
    else:
        print("\nyou are in global enviroment")


def main() -> int:
    """
    "numpy" #np
    "pandas" #pd
    "matplotlib" #plt
    requests" #req
    """
    ft_vm()
    np, pd, plt, req = ft_run_impoter()
    acceleration = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    a = np.empty((9, 10), dtype=np.dtype("B"))
    df = pd.DataFrame(a, columns=acceleration)

    fig, ax = plt.subplots(1, figsize=(10, 4))
    ax.imshow(a, cmap="viridis")
    ax.set_title("result")
    plt.tight_layout()
    plt.savefig("matrix.png")
    plt.show()
    plt.close(fig)
    print("")
    print(df)
    print('\n***result saved as "matrix.png"***')
    return 0


if __name__ == "__main__":
    sys.exit(main())
