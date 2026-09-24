from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    allowed = ["earth", "air", "fire", "water"]
    return (allowed)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        spell = "spell rejected: " + spell_name + " " + result
        return (spell)
    spell = "spell recorded: " + spell_name + " " + result
    return (spell)
