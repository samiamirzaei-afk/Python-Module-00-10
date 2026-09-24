from abc import ABC, absstractmethod

class Creature(ABC):
    def __init__(self) -> None:
        self.name = pass
        self.type = pass

    def describe(self) -> str:
        result = self.name + " is a " + self.type + " type Creature"
        return (result)

    @absstractmethod
    def attack() -> str:
        pass

class CreatureFactory(ABC):

    @absstractmethod
    def create_base()

    @absstractmethod
    def create_evolved()


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"

    def attack() -> str:
        result = self.name + " uses Ember"
        return(result)


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Flying"

    def attack() -> str:
        result = self.name + " uses Flamethrower"
        return(result)


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Aquabub"
        self.type = "Water"

    def attack() -> str:
        result = self.name + " uses Water Gun"
        return(result)


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"

    def attack() -> str:
        result = self.name + " uses Hydro Pump"
        return(result)


def main() -> int:



if __name__ == "__main__":
    _ = main()
