def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingredients = ingredients.lower()
    allowed = light_spell_allowed_ingredients()
    if ingredients in allowed:
        verdict = "VALID"
    else:
        verdict = "INVALID"

    result = ingredients + " - " + verdict
    return(result)
