import ex0
import ex1


def fac_show(fac: ex0.CreatureFactory) -> None:
    if isinstance(fac, ex0.CreatureFactory) is False:
        print(fac, "can't make pokees!")
        return
    if isinstance(fac, ex1.TransformCreatureFactory) is True:
        pokee = fac.create_base()
        print(pokee.attack())
        print(pokee.transform())
        print(pokee.attack())
        print(pokee.revert())
        print("* evolve *")
        pokee = fac.create_evolved()
        print(pokee.attack())
        print(pokee.transform())
        print(pokee.attack())
        print(pokee.revert())
        return
    pokee = fac.create_base()
    print(pokee.attack())
    print(pokee.heal("itself"))
    pokee = fac.create_evolved()
    print(pokee.attack())
    print(pokee.heal("itself and others"))
    return


def fac_maker(fac: ex0.CreatureFactory) -> None:
    if isinstance(fac, ex0.CreatureFactory) is False:
        print(fac, "can't make pokees!")
        return

    poke = fac.create_base()
    result = poke.attack()
    result2 = poke.describe()
    print(result)
    print(result2)
    print("* evolve *")
    poke = fac.create_evolved()
    result = poke.attack()
    result2 = poke.describe()
    print(result)
    print(result2)
    print("")


def main() -> int:
    flame = ex1.HealingCreatureFactory()
    aqua = ex1.TransformCreatureFactory()
#    fake: ex0.CreatureFactory = "lol"
    fac_maker(flame)
    fac_maker(aqua)
    fac_show(flame)
    fac_show(aqua)
    '''
    print("now bad tests")
    fac_show(fake, aqua)
    fac_show(aqua, fake)

    fac_maker(fake)
    '''
    return (1)


if __name__ == "__main__":
    _ = main()
