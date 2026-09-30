from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    def describe(self) -> str:
        result: str = self.name + " is a " + self.type + " type Creature"
        return result

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        result = self.name + " uses Ember"
        return result


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        result = self.name + " uses Flamethrower"
        return result


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        result = self.name + " uses Water Gun"
        return result


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        result = self.name + " uses Hydro Pump"
        return result
