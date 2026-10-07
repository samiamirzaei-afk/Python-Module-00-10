import sys
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env from the current directory (or parents)


def ft_developer() -> None:
    empty: str | None = ""
    d_env = {
        "DATABASE_URL": empty,
        "API_KEY": empty,
        "LOG_LEVEL": empty,
        "ZION_ENDPOINT": empty,
    }
    fail = False
    d_env["DATABASE_URL"] = os.getenv("DATABASE_URL")
    d_env["API_KEY"] = os.getenv("API_KEY")
    d_env["LOG_LEVEL"] = os.getenv("LOG_LEVEL")
    d_env["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT")

    for key, value in d_env.items():
        if value in [None, ""]:
            print(key, "is missing!")
            fail = True

    if fail:
        print("\naborting program")
        return
    print("DATABASE_URL:", d_env["DATABASE_URL"])
    print("API_KEY:", d_env["API_KEY"])
    print("LOG_LEVEL:", d_env["LOG_LEVEL"])
    print("ZION_ENDPOINT:", d_env["ZION_ENDPOINT"])
    print("\nIn Dev mode, do not use this mode in production!")


def ft_production() -> None:
    print("in production mode:")


def main() -> int:
    mode = os.getenv("MATRIX_MODE", "production_default").lower()
    print("current mode:", mode)
    if mode == "development":
        ft_developer()
    elif mode == "production":
        ft_production()
    elif mode == "production_default":
        print("defaulting to production mode:")
        ft_production()
    else:
        print("write it correctly idiot")
    return 0


if __name__ == "__main__":
    sys.exit(main())
