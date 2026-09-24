from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed = ["bats", "frogs", "arsenic", "eyeball"]
    return (allowed)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        spell = "spell rejected: " + spell_name + " " + result
        return (spell)
    spell = "spell recorded: " + spell_name + " " + result
    return (spell)
