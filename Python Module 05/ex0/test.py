from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    '''
    def __init__(self) -> None:
        self.storage: list[str] = list()
        self.index = 0
    '''

    def output(self) -> tuple[int, str]:
        check = len(self.storage)
        if check == 0:
            return -1, "list is empty, out of values"
        result = self.storage.pop(0)
        self.index += 1
        return self.index - 1, result

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


def ft_print(mode: int, data: Any) -> None:
    if mode != 1:
        return
    print(data)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.storage: list[str] = list()
        self.index = 0
        pass

    def show_storage(self) -> None:
        print(self.storage)

    def validate(self, data: Any) -> bool:
        if isinstance(data, (bool, dict, tuple, str, set)):
            return False
        if isinstance(data, (int, float)):
            ft_print(0, data="is a number!")
            return True

        if isinstance(data, (list)):
            for section in data:
                if isinstance(section, bool):
                    return (False)
                if isinstance(section, (int, float)):
                    continue
                ft_print(0, data=[section, "is not a number!"])
                return(False)
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise ValueError(f"{data} is not valid")
        if isinstance(data, list):
            for section in data:
                self.storage.append(str(section))
            return
        self.storage.append(data)
        return


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.storage: list[str] = list()
        self.index = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, (bool, dict, tuple, set, int, float)):
            return False
        if isinstance(data, (str)):
            ft_print(0, data="is a string!")
            return True

        if isinstance(data, (list)):
            for section in data:
                if isinstance(section, (str)):
                    continue
                ft_print(0, data=[section, "is not a string!"])
                return(False)
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise ValueError(f"{data} is not valid")
        if isinstance(data, list):
            for section in data:
                self.storage.append(section)
                print(section, "is added")
            return
        print(data, "is added")
        self.storage.append(data)
        return

    def show_storage(self) -> None:
        print(self.storage)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self.storage: list[str] = list()
        self.index = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float, str, set, bool, tuple)):
            return (False)
        if isinstance(data, (dict)):
            for k, v in data.items():
                result_k = isinstance(k, str)
                result_v = isinstance(v, str)
                if result_k is True and result_v is True:
                    continue
                return (False)
            return(True)
        if isinstance(data, list):
            for section in data:
                if isinstance(section, (int, float, str, set, bool, tuple)):
                    return (False)
                if isinstance(section, dict):
                    result = self.validate(section)
                    if result is False:
                        return (False)
            return (True)
        return (False)

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise ValueError(f"{data} is not valid")
        if isinstance(data, list):
            for section in data:
                for value in section.values():
                    self.storage.append(value)
            return
        print(data, "is added")
        for section in data.values():
            self.storage.append(section)
        return

        pass

    def show_storage(self) -> None:
        print(self.storage)

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
            print()
            print("ingesting", big)
            lol.ingest(big)
            try:
                print("ingesting", big3)
                lol.ingest(big3)
            except ValueError as e:
                print(e)
                lol.show_storage()
            lol.show_storage()
            action = input("fail the funtion?(Yes/No?):").strip().lower()
            if action in {"yes", "y"}:
                print("failing....")
                try:
                    lol.ingest(big2)
                    lol.ingest(big4)
                    lol.show_storage()
                except ValueError as e:
                    print(e)
                lol.show_storage()
                for i in range(10):
                    result = lol.output()
                    print(result)
                return (0)
            return(0)

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
            lol.ingest(big2)
            lol.ingest(big6)
            lol.show_storage()
            print()
            action = input("fail the funtion?(Yes/No?):").strip().lower()
            if action in {"yes", "y"}:
                print("failing....")
                try:
                    lol.ingest(big)
                    lol.ingest(big4)
                    lol.show_storage()
                except ValueError as e:
                    print(e)
                lol.show_storage()
                for i in range(10):
                    result = lol.output()
                    print(result)
                return (0)

        case 3:
            people = [
                {"name": "Alice", "age": 30, "city": "Vienna"},
                {"name": "Bob", "age": 25, "city": "Berlin"},
                {"name": "Charlie", "age": "35", "city": "Paris"},
                    ]
            lol = LogProcessor()
            result = lol.validate(people)
            print(people, result)
            people_2 = [
                {"name": "Alice", "age": "30", "city": "Vienna"},
                {"name": "Bob", "age": "25", "city": "Berlin"},
                {"name": "Charlie", "age": "35", "city": "Paris"},
                    ]
            result = lol.validate(people_2)
            print(people_2, result)
            people_3 = {"input_1": "test", "input_2": "test",
                        "input_3": "test", "input_4": "test",
                        "input_5": "test", "input_6": "test",
                        "input_7": "test", "input_8": "test",}
            result = lol.validate(people_3)
            print(people_3, result)
            people_4 = {"input_1": "test", "input_2": "test",
                        "input_3": "test", "input_4": "test",
                        "input_5": "test", "input_6": "test",
                        "input_7": "test", "input_8": 1}
            result = lol.validate(people_4)
            print(people_4, result)
            result = lol.validate(big6)
            print(result)
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
            lol.ingest(people_2)
            action = input("fail the funtion?(Yes/No?):").strip().lower()
            if action in {"yes", "y"}:
                print("failing....")
                try:
                    lol.ingest(big)
                    lol.ingest(big4)
                    lol.show_storage()
                except ValueError as e:
                    print(e)
                lol.show_storage()
                for i in range(10):
                    result = lol.output()
                    print(result)
                    print(result[1], "is a", type(result[1]))
                lol.ingest(people_3)
                lol.show_storage()
                for i in range(10):
                    result = lol.output()
                    print(result)
                    print(result[1], "is a", type(result[1]))
                return (0)


        case _:
            print("no correct case was given")
            return(0)
    return(0)

if __name__ == "__main__":
    _ = main()




#should this be fine?
    '''
    def ingest(self, data: Any) -> None:
        try:
            if isinstance(data, str):
                self.storage.append(str(data))
            if isinstance(data, list):
                for section in data:
                    self.storage.append(str(section))
            return
        except ValueError as e:
            print("**ingest failed**")
            raise e
    
    def ingest(self, data: Any) -> None:
            if isinstance(data, (int, float, dict, set, tuple, bool)):
                raise ValueError(f"{type(data)} is not valid")
                self.storage.append(str(data))
            if isinstance(data, str):
                self.storage.append(str(data))
            if isinstance(data, list):
                for section in data:
                    if isinstance(section, (int, float, dict, set, tuple, bool)):
                        raise ValueError(f"{type(section)} is not valid")
                    self.storage.append(section)
            return
    '''
