from .elements import create_air, create_earth
from elements import create_water, create_fire


def healing_potion() -> str:
    air = create_air()
    earth = create_earth()
    healing = "healing potion brewed with[" + air + "][" + earth + "]"
    return (healing)


def strength_potion() -> str:
    water = create_water()
    fire = create_fire()
    strength = "strength potion brewed with[" + water + "][" + fire + "]"
    return (strength)
