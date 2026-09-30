import ex2
from autobahn.wamp.gen.wamp.proto.Result import Result
from typing import Any, cast
from abc import ABC, abstractmethod
import ex0
import ex1


class StratError(Exception):
    def __init__(self, message) -> None:
        if message == "":
            self.message = "missmatch type and BattleStrategy"
        else:
            self.message = message


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, pokee: ex0.Creature) -> bool:
        pass

    @abstractmethod
    def act(self, pokee: ex0.Creature) -> list[str]:
        pass


class HealCreature(ex0.Creature, ex1.HealCapability):
    pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, pokee: ex0.Creature) -> bool:
        if isinstance(pokee, ex0.Creature):
            return True
        return False

    def act(self, pokee: ex0.Creature) -> list[str]:
        if self.is_valid(pokee) is False:
            raise (StratError)
        result = []
        result.append(pokee.attack())
        return result


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, pokee: ex0.Creature) -> bool:
        return isinstance(pokee, ex1.TransformCapability)

    def act(self, pokee: Any) -> list[str]:
        if self.is_valid(pokee) is False:
            raise (StratError)
        result = []
        result.append(pokee.transform())
        result.append(pokee.attack())
        result.append(pokee.revert())
        return result


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, pokee: ex0.Creature) -> bool:
        if isinstance(pokee, ex1.HealCapability) is True:
            return True
        elif isinstance(pokee, ex1.HealCapability) is False:
            return False
        return False

    def act(self, pokee: ex0.Creature) -> list[str]:
        if self.is_valid(pokee) is False:
            raise StratError
        pokee = cast(HealCreature, pokee)
        result = []
        result.append(pokee.attack())
        result.append(pokee.heal("itself"))
        return result
