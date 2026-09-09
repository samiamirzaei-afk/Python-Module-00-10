class Plant:
    def __init__(self, water_level: int, name: str = "placeholder") -> None:
        self.name = name
        self.water_level = water_level


class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant error") -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water error") -> None:
        self.message = message
        super().__init__(self.message)


def water_check(p1: Plant) -> None:
    if p1.water_level > 8 or p1.water_level < 1:
        raise WaterError(f"{p1.name} WaterError: {p1.water_level} liters"
                         " is bad, it should be between 8-1 liters")
    print(f"{p1.name} passed water_check")


def name_check(p1: Plant) -> None:

    if not (p1.name == "olive" or p1.name == "tomato"):
        raise PlantError()
    print(f"{p1.name} passed name_check")


def all_check(p1: Plant) -> None:
    water_check(p1)
    water_check(p2)
    water_check(p3)
    name_check(p1)
    name_check(p2)
    name_check(p3)


def testing_sep(p1: Plant, p2: Plant, p3: Plant) -> None:

    try:
        water_check(p1)
    except WaterError as e:
        print(e)
    try:
        water_check(p2)
    except WaterError as e:
        print(e)
    try:
        water_check(p3)
    except WaterError as e:
        print(e)
    print("\n")
    try:
        name_check(p1)
    except PlantError as e:
        print(e)
    try:
        name_check(p2)
    except PlantError as e:
        print(e)
    try:
        name_check(p3)
    except PlantError as e:
        print(e)

    print("=== now all check ===")
    try:
        all_check(p1)
        all_check(p2)
        all_check(p3)
    except GardenError as e:
        print(f"GardenError: {e}")


if __name__ == "__main__":
    p1 = Plant(10, "tomato")
    p2 = Plant(3, "olive")
    p3 = Plant(6, "cherry")

    testing_sep(p1, p2, p3)
    print("\n== end of program ==")
