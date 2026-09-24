from elements  import create_fire as el
from ..elements import create_air
from ..potions import strength_potion

def lead_to_gold() -> str:
    air =create_air()
    str_potion = strength_potion()
    fire = el()
    gold = "Gold: brew:" + air + " and " + str_potion + " mixed with " + fire
    return(gold)
