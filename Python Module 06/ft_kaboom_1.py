from alchemy.grimoire.dark_spellbook import dark_spell_record

if __name__ == "__main__":
    result = dark_spell_record("testing", "fire")
    print(result)
    result = dark_spell_record("testing", "book")
    print(result)
    result = dark_spell_record("testing", "frog")
    print(result)
