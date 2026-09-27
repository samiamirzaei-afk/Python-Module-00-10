from abc import ABC, abstractmethod
import ex0


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(ex0.Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Sproutling"
        self.type = "Grass"

    def attack(self) -> str:
        result = self.name + " uses Vine Whip"
        return (result)

    def heal(self, target: str) -> str:
        result = self.name + " heals " + target + " for a small ammout"
        return (result)


class Bloomelle(ex0.Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"

    def attack(self) -> str:
        result = self.name + "uses Petal Dance"
        return (result)

    def heal(self, target: str) -> str:
        result = self.name + " heals " + target + " for a small ammout"
        return (result)


class Shiftling(ex0.Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Shiftling"
        self.type = "Normal"
        self.trans = False

    def attack(self) -> str:
        if self.trans is False:
            result = self.name + " attacks normally"
            return (result)
        result = self.name + " uses morph strike"
        return (result)

    def transform(self) -> str:
        result = self.name + " shifts into a sharper form"
        self.trans = True
        return (result)

    def revert(self) -> str:
        result = self.name + " motphs back to normal"
        self.trans = False
        return (result)


class Morbius(ex0.Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Morbius"
        self.type = "normal/morb"
        self.morbin_time = False

    def attack(self) -> str:
        if self.morbin_time is False:
            result = self.name + " attacks normally"
            return (result)
        result = self.name + " Morbs you to death"
        return (result)

    def transform(self) -> str:
        result = self.name + ": \"Its morbin time\""
        self.morbin_time = True
        return (result)

    def revert(self) -> str:
        result = self.name + " excels to have sex"
        self.morbin_time = False
        return (result)
