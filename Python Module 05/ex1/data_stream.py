from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = list()
        self.total_op = 0
        self.current_op = 0
        self.index = 0

    def output(self) -> tuple[int, str]:
        check = len(self.storage)
        if check == 0:
            self.index = 0
            return -1, "list is empty, out of values"
        result = self.storage.pop(0)
        self.index += 1
        self.current_op -= 1
        return self.index - 1, result

    def input(self, count: int) -> None:
        self.total_op += count
        self.current_op += count

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class DataStream:
    def __init__(self) -> None:
        self.processor_list: list[DataProcessor] = list()

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for proc in self.processor_list:
                if proc.validate(item) is True:
                    proc.ingest(item)
                    print(item, "was added to", proc.__class__.__name__)
                    if isinstance(item, (list, dict)):
                        count = len(item)
                        proc.input(count)
                    else:
                        proc.input(1)
                    break
                else:
                    print(item, "does not fit into", proc.__class__.__name__)

    def print_processors_stats(self) -> None:
        if not self.processor_list:
            print("no processes found")
            return
        for proc in self.processor_list:
            name = proc.__class__.__name__
            print(f"{name}, {proc.total_op=}, {len(proc.storage)} left")
            print(f"{proc.storage}")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def show_storage(self) -> None:
        print(self.storage)

    def validate(self, data: Any) -> bool:
        if isinstance(data, (bool, dict, tuple, str, set)):
            return False
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, (list)):
            for section in data:
                if isinstance(section, bool):
                    return (False)
                if isinstance(section, (int, float)):
                    continue
                return (False)
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
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (bool, dict, tuple, set, int, float)):
            return False
        if isinstance(data, (str)):
            return True

        if isinstance(data, (list)):
            for section in data:
                if isinstance(section, (str)):
                    continue
                return (False)
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise ValueError(f"{data} is not valid")
        if isinstance(data, list):
            for section in data:
                self.storage.append(section)
            return
        print(data, "is added")
        self.storage.append(data)
        return

    def show_storage(self) -> None:
        print(self.storage)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

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
            return (True)
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
    stream = DataStream()
    test_mode = int(input("Are you Ready? (Type 1): "))
    big = [1, 2, 3, 4, 5, 6]
    big1 = [1982741987]
    big2 = ["goofy"]
    big3 = [1, 2, 43, "lol", 14]
    big4 = [True]
    big5 = [1, 2, 43, True, 14]
    big6 = ["obama", "osama", "kirkbama"]
    big7 = ["obama", "osama", 13]
    match test_mode:
        case 1:
            action = input("add NumericProcessor?(Yes/No?)").strip().lower()
            if action in {"yes", "y"}:
                stream = DataStream()
                stream.register_processor(NumericProcessor())
                stream.process_stream(big)
                stream.process_stream(big1)
                stream.process_stream(big2)
                stream.process_stream(big3)
                stream.process_stream(big4)
                stream.process_stream(big5)
                stream.process_stream(big6)
                stream.process_stream(big7)
                stream.print_processors_stats()
            action = input("print output?(Yes/No?)").strip().lower()
            if action in {"yes", "y"}:
                for i in range(13):
                    result = stream.processor_list[0].output()
                    print(result)
                    stream.print_processors_stats()
                action = input("keep outputting?(Yes/No?)").strip().lower()
                if action in {"yes", "y"}:
                    for i in range(13):
                        result = stream.processor_list[0].output()
                        print(result)
                        stream.print_processors_stats()
            action = input("add TextProcessor?(Yes/No?)").strip().lower()
            if action in {"yes", "y"}:
                stream.register_processor(TextProcessor())
                stream.process_stream(big)
                stream.process_stream(big1)
                stream.process_stream(big2)
                stream.process_stream(big3)
                stream.process_stream(big4)
                stream.process_stream(big5)
                stream.process_stream(big6)
                stream.process_stream(big7)
                stream.print_processors_stats()
                action = input("print outputting?(Yes/No?)").strip().lower()
                if action in {"yes", "y"}:
                    for i in range(13):
                        result = stream.processor_list[1].output()
                        print(result)
                        stream.print_processors_stats()
                    action = input("keep outputting?(Yes/No?)").lower()
                    if action in {"yes", "y"}:
                        for i in range(13):
                            result = stream.processor_list[1].output()
                            print(result)
                            stream.print_processors_stats()
            action = input("add LogProcessor?(Yes/No?)").strip().lower()
            if action in {"yes", "y"}:
                people = [
                    {"name": "Alice", "age": 30, "city": "Vienna"},
                    {"name": "Bob", "age": 25, "city": "Berlin"},
                    {"name": "Charlie", "age": "35", "city": "Paris"},
                        ]
                stream.register_processor(LogProcessor())
                stream.process_stream(people)
                people_2 = [
                    {"name": "Alice", "age": "30", "city": "Vienna"},
                    {"name": "Bob", "age": "25", "city": "Berlin"},
                    {"name": "Charlie", "age": "35", "city": "Paris"},
                        ]
                stream.process_stream(people_2)
#                people_3 = {"input_1": "test", "input_2": "test",
#                            "input_3": "test", "input_4": "test",
#                            "input_5": "test", "input_6": "test",
#                            "input_7": "test", "input_8": "test"}
#                stream.process_stream(people_3)
#                people_4 = {"input_1": "test", "input_2": "test",
#                            "input_3": "test", "input_4": "test",
#                            "input_5": "test", "input_6": "test",
#                            "input_7": "test", "input_8": 1}
#                stream.process_stream(people_4)
                stream.process_stream(big)
                stream.process_stream(big1)
                stream.process_stream(big2)
                stream.print_processors_stats()
                action = input("print outputting?(Yes/No?)").strip().lower()
                if action in {"yes", "y"}:
                    for i in range(13):
                        result = stream.processor_list[2].output()
                        print(result)
                        stream.print_processors_stats()
                    action = input("keep outputting?(Yes/No?)").lower()
                    if action in {"yes", "y"}:
                        for i in range(13):
                            result = stream.processor_list[2].output()
                            print(result)
                            stream.print_processors_stats()
        case _:
            print("no correct case was given")
            return (0)
    return (0)


if __name__ == "__main__":
    try:
        _ = main()
    except BaseException as e:
        print(e)
