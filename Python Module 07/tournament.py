import ex0
import ex1
import ex2


def fightmode(ops: tuple[ex0.CreatureFactory, ex2.BattleStrategy]) -> None:
    pokee_facttory, pokee_attack = ops
    pokee = pokee_facttory.create_base()
    result = []
    if isinstance(pokee_attack, ex2.NormalStrategy):
        result.append(pokee.attack())
        for i in result:
            print(i)
        return
    if isinstance(pokee_attack, ex2.AggressiveStrategy):
        if isinstance(pokee_facttory, ex1.TransformCreatureFactory) is False:
            print(
                pokee.__class__.__name__,
                "is not",
                ex1.TransformCreatureFactory.__name__,
            )
            raise ex2.StratError("missmatch type and BattleStrategy")
        temp = pokee_attack.act(pokee)
        result = result + temp
        for i in result:
            print(i)
        return
    if isinstance(pokee_attack, ex2.DefensiveStrategy):
        if isinstance(pokee_facttory, ex1.HealingCreatureFactory) is False:
            print(
                pokee.__class__.__name__, "is not",
                ex1.HealingCreatureFactory.__name__
            )
            raise ex2.StratError("missmatch type and BattleStrategy")
        temp = pokee_attack.act(pokee)
        result = result + temp
        for i in result:
            print(i)
        return


def ft_show_ops(ops: list[tuple[ex0.CreatureFactory,
                                ex2.BattleStrategy]]) -> None:
    name = [(C.__class__.__name__, B.__class__.__name__) for C, B in ops]
    print(name)


def battle(ops: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]) -> int:
    result = len(ops)
    print(result, "opponents added:")
    ft_show_ops(ops)
    if result < 2:
        print("single Pokee has no one to fight!")
        return 1

    while 1:
        current = ops.pop(0)
        if len(ops) == 0:
            return 0
        current_factory, _ = current
        current_pokee = current_factory.create_base()
        for fighter in ops:
            fighter_factory, _ = fighter
            fighter_pokee = fighter_factory.create_base()
            print("")
            print(current_pokee.describe())
            print("VS.")
            print(fighter_pokee.describe())
            print("* Fight *")
            try:
                fightmode(current)
                fightmode(fighter)
            except ex2.StratError as e:
                print(e)
                return 1
            print("NEXT FIGHT!\n")


def main() -> int:
    """
    flame = ex0.FlameFactory().create_base()
    flame_plus = ex0.FlameFactory().create_evolved()
    aqua = ex0.AquaFactory().create_base()
    aqua_plus = ex0.AquaFactory().create_evolved()

    heal = ex1.HealingCreatureFactory().create_base()
    heal_plus = ex1.HealingCreatureFactory().create_evolved()
    morb = ex1.TransformCreatureFactory().create_base()
    morb_plus = ex1.TransformCreatureFactory().create_evolved()
    """
    normal = ex2.NormalStrategy()
    defen = ex2.DefensiveStrategy()
    agro = ex2.AggressiveStrategy()

    battle([(ex0.AquaFactory(), normal), (ex0.AquaFactory(), agro)])
    battle([(ex0.AquaFactory(), normal), (ex0.AquaFactory(), defen)])
    battle(
        [(ex1.TransformCreatureFactory(), agro),
         (ex1.HealingCreatureFactory(), normal)]
    )

    battle(
        [(ex1.HealingCreatureFactory(), defen),
         (ex1.HealingCreatureFactory(), normal)]
    )
    battle(
        [(ex1.HealingCreatureFactory(), defen),
         (ex1.TransformCreatureFactory(), agro)]
    )
    print("---\n")
    battle(
        [
            (ex1.HealingCreatureFactory(), defen),
            (ex0.FlameFactory(), normal),
            (ex0.AquaFactory(), normal),
            (ex1.TransformCreatureFactory(), agro),
        ]
    )
    battle([(ex0.FlameFactory(), normal), (ex0.FlameFactory(), agro)])
    battle([(ex0.FlameFactory(), normal), (ex0.FlameFactory(), defen)])
    return (0)


if __name__ == "__main__":
    _ = main()
