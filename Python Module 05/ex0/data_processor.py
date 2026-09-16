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


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        pass

    def validate(self, data: Any) -> bool:
        


class TextProcessor(DataProcessor):
    pass

class LogProcessor(DataProcessor):
    pass


def main() -> int:


if __name__ == "__main__":
    _ = main()
