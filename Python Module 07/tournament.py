from abc import ABC, abstractmethod
from typing import Any
import ex0
import ex1
import ex2

def st_finder(op:tuple[ex0.CreatureFactory, ex2.BattleStrategy]) -> list[str]:
        pokee, pokee_attack = op
        result = []
        if pokee_attack == ex2.NormalStrategy:
            result.append(pokee.describe())
            result.append(pokee.attack())
            return (result)
        if pokee_attack == ex2.AggressiveStrategy:
            if isinstance(pokee, TransformCreatureFactory) is False:
                raise StratError("missmatch type and BattleStrategy")
            result.append(pokee.describe())
            temp = pokee.act()
            result = result + temp
            return (result)
        if pokee_attack == ex2.NormalStrategy:
            if isinstance(pokee, HealingCreatureFactory) is False:
                raise StratError("missmatch type and BattleStrategy")
            result.append(pokee.describe())
            temp = pokee.act()
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
            except StratError as e:
                print(e)
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
                (heal, passive)])
    battle([(flame, agro),
                (heal, passive)])
    battle([(aqua, normal),
                (heal, passive),
                (morb_plus, agro)])


if __name__ == "__main__":
    _ = main()

