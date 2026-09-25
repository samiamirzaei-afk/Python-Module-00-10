import ex0


def fac_fighter(fac1: ex0.CreatureFactory, fac2: ex0.CreatureFactory) -> None:
    if isinstance(fac1, ex0.CreatureFactory) is False:
        print(fac1, "can't make pokees!")
        return
    if isinstance(fac2, ex0.CreatureFactory) is False:
        print(fac2, "can't make pokees!")
        return
    pokee1 = fac1.create_base()
    pokee2 = fac2.create_base()

    print(pokee1.describe())
    print(" vs.")
    print(pokee2.describe())
    print(" fight!")
    print(pokee1.attack())
    print(pokee2.attack())


def fac_maker(fac: ex0.CreatureFactory) -> None:
    if isinstance(fac, ex0.CreatureFactory) is False:
        print(fac, "can't make pokees!")
        return

    poke = fac.create_base()
    result = poke.attack()
    result2 = poke.describe()
    print(result)
    print(result2)
    print()
    poke = fac.create_evolved()
    result = poke.attack()
    result2 = poke.describe()
    print(result)
    print(result2)


def main() -> int:
    flame = ex0.FlameFactory()
    aqua = ex0.AquaFactory()
#    fake: ex0.CreatureFactory = "lol"
    fac_maker(flame)
    fac_maker(aqua)
    fac_fighter(flame, aqua)
    '''
    print("now bad tests")
    fac_fighter(fake, aqua)
    fac_fighter(aqua, fake)

    fac_maker(fake)
    '''
    return (1)

if __name__ == "__main__":
    _ = main()
