from abc import ABC, abstractmethod
import ex0
import ex1


class StratError(Exception):
    def __init__(self) -> None:
        self.message = "missmatch type and BattleStrategy"

class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, pokee: ex0.Creature) -> bool:
        pass

    @abstractmethod
    def act(self) -> None:
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, pokee: ex0.Creature) -> bool:
        if isinstance(pokee, ex0.Creature) is True:
            return (True)
        return (False)

    def act(self, pokee: ex0.Creature) -> list[str]:
        result = []
        result.append(pokee.attack())
        return(result)

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, pokee: ex0.Creature) -> bool:
        if isinstance(pokee, ex1.TransformCapability) is True:
            return (True)
        return (False)

    def act(self, pokee: ex1.TransformCapability) -> list[str]:
        result = []
        result.append(transform())
        result.append(pokee.attack())
        result.append(pokee.revert())
        return (result)


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, pokee: ex0.Creature) -> bool:
        if isinstance(pokee, ex1.HealCapability) is True:
            return (True)
        return (False)

    def act(self, pokee: ex1.HealCapability) -> list[str]:
        result = []
        result.append(pokee.attack())
        result.append(pokee.heal("itself"))
        return (result)

