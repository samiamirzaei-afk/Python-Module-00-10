import ex0
from .Pokees import Sproutling, Bloomelle, Shiftling, Morbius


class HealingCreatureFactory(ex0.CreatureFactory):
    def create_base(self) -> ex0.Creature:
        return Sproutling()

    def create_evolved(self) -> ex0.Creature:
        return Bloomelle()


class TransformCreatureFactory(ex0.CreatureFactory):
    def create_base(self) -> ex0.Creature:
        return Shiftling()

    def create_evolved(self) -> ex0.Creature:
        return Morbius()
