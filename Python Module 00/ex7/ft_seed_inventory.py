def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packet":
        print(f"{seed_type} seeds: {quantity} packets available")
        return
    if unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
        return
    if unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
        return
    print("Unknown unit type")
