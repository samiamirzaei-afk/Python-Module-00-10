from abc import ABC, abstractmethod
from typing import Any
import ex0
import ex1
import ex2

def st_finder(op:tuple[ex0.CreatureFactory, ex2.BattleStrategy]) -> list[str]:
        pokee, pokee_attack = op
        result = []
        if isinstance (pokee_attack,  ex2.NormalStrategy):
            result.append(pokee.describe())
            result.append(pokee.attack())
            return (result)
        if isinstance(pokee_attack, ex2.AggressiveStrategy):
            if isinstance(pokee, ex1.TransformCreatureFactory) is False:
                print(pokee.__class__.__name__, "is not", ex1.HealingCreatureFactory.__name__)
                raise ex2.StratError("missmatch type and BattleStrategy bob")
            result.append(pokee.describe())
            temp = pokee_attack.act(pokee)
            result = result + temp
            return (result)
        if isinstance (pokee_attack, ex2.DefensiveStrategy):
            if isinstance(pokee, ex1.HealingCreatureFactory) is False:
                print(pokee.__class__.__name__, "is not", ex1.HealingCreatureFactory.__name__)
                raise ex2.StratError("missmatch type and BattleStrategy lol")
            result.append(pokee.describe())
            temp = pokee_attack.act(pokee)
            result = result + temp
            return (result)

def battle(ops: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]) -> int:
    result: Any = len(ops)
    print(result, "opponets added")
    if result < 2:
        print("single Pokee has no one to fight!")
        return (1)
    while(1):
        current = ops.pop(0)
        if len(ops) == 0:
            return (0)
        for fighter in ops:
            print("* Fight *")
            try:
                pokee1 = st_finder(current)
                pokee2 = st_finder(fighter)
            except ex2.StratError as e:
                print(e)
                return (1)
            print(pokee1)
            print(pokee2)
            
        

def main() -> int:
    flame = ex0.FlameFactory().create_base()
    flame_plus = ex0.FlameFactory().create_evolved()
    aqua = ex0.AquaFactory().create_base()
    aqua_plus = ex0.AquaFactory().create_evolved()

    heal = ex1.HealingCreatureFactory().create_base()
    heal_plus = ex1.HealingCreatureFactory().create_evolved()
    morb = ex1.TransformCreatureFactory().create_base() 
    morb_plus = ex1.TransformCreatureFactory().create_evolved()

    normal = ex2.NormalStrategy()
    passive = ex2.DefensiveStrategy()
    agro = ex2.AggressiveStrategy()
    battle([(flame, normal),
                (morb_plus, agro)])
    battle([(flame, agro),
                (heal, passive)])
    battle([(aqua, normal),
                (heal, passive),
                (morb_plus, agro)])


if __name__ == "__main__":
    _ = main()

