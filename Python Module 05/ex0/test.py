from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def output(self) -> tuple[int, str]:
        pass


    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

def ft_print(mode, data) -> None:
        if mode != 1:
            return
        print(data)

class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        pass
    


    def validate(self, data: Any) -> bool:
        if isinstance(data, (bool, dict, tuple, str, set)):
            return False
        if isinstance(data, (int, float)):
            ft_print(0, data = "is a number!")
            return True

        if isinstance(data, (list)):
            for section in data:
                if isinstance(section, bool):
                    return (False)
                if isinstance(section, (int, float)):
                    continue
                ft_print(0, data =[section, "is not a number!"])
                return(False)
            return True
        return False

    def ingest(self, data: Any) -> None:
        pass

class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        pass

    def validate(self, data: Any) -> bool:
        if isinstance(data, (bool, dict, tuple, set, int, float)):
            return False
        if isinstance(data, (str)):
            ft_print(0, data = "is a string!")
            return True

        if isinstance(data, (list)):
            for section in data:
                if isinstance(section, (str)):
                    continue
                ft_print(0, data =[section, "is not a string!"])
                return(False)
            return True
        return False

    def ingest(self, data: Any) -> None:
        pass


def main() -> int:

    test_mode = int(input("which case to test? numbs, strings, dics? (1, 2, 3): "))
    big = [1, 2, 3, 4, 5, 6]
    big1 = 1982741987
    big2 = "goofy"
    big3 = [1, 2, 43, "lol", 14]
    big4 = True
    big5 = [1, 2, 43, True, 14]
    big6 = ["obama", "osama", "kirkbama"]
    big7 = ["obama", "osama", 13]
    match test_mode:
        case 1:
            lol = NumericProcessor()
            result = lol.validate(big)
            print(big, result)
            result = lol.validate(big1)
            print(big1, result)
            result = lol.validate(big2)
            print(big2, result)
            result = lol.validate(big3)
            print(big3, result)
            result = lol.validate(big4)
            print(big4, result)
            result = lol.validate(big5)
            print(big5, result)
            result = lol.validate(big6)
            print(big6, result)
            result = lol.validate(big7)
            print(big7, result)
        case 2:
            lol = TextProcessor() 
            result = lol.validate(big)
            print(big, result)
            result = lol.validate(big1)
            print(big1, result)
            result = lol.validate(big2)
            print(big2, result)
            result = lol.validate(big3)
            print(big3, result)
            result = lol.validate(big4)
            print(big4, result)
            result = lol.validate(big5)
            print(big5, result)
            result = lol.validate(big6)
            print(big6, result)
            result = lol.validate(big7)
            print(big7, result)
        case _:
            print("no correct case was given")
            return(0)


if __name__ == "__main__":
    _ = main()
