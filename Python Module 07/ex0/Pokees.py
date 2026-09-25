from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        self.name: str = ""
        self.type: str = ""

    def describe(self) -> str:
        result: str = self.name + " is a " + self.type + " type Creature"
        return (result)

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        result = self.name + " uses Ember"
        return (result)


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack(self) -> str:
        result = self.name + " uses Flamethrower"
        return (result)


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Aquabub"
        self.type = "Water"

    def attack(self) -> str:
        result = self.name + " uses Water Gun"
        return (result)


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"

    def attack(self) -> str:
        result = self.name + " uses Hydro Pump"
        return (result)
