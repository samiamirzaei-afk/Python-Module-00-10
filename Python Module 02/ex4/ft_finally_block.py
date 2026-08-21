class Plant:
    def __init__(self, water_level: int, name: str = "placeholder") -> None:
        self.name = name
        self.water_level = water_level


class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden error") -> None:
        self.message = message
        super().__init__(self.message)
#   why do self.message and not just message?


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant error") -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:

    if not plant_name == plant_name.capitalize():
        raise PlantError(f"{plant_name} not capitalized")
    print(f"{plant_name} was watered")


def test_watering_system(p1: Plant, p2: Plant, p3: Plant) -> None:
    print("Opening water system")
    try:
        water_plant(p1.name)
        water_plant(p2.name)
    except GardenError as e:
        print(f"{e} -- water-system failure!")
    finally:
        print("Closing water system")


if __name__ == "__main__":
    p1 = Plant(10, "Tomato")
    p2 = Plant(3, "Olive")
    p3 = Plant(3, "Cucumber")
    p4 = Plant(6, "cherry")

    test_watering_system(p1, p2, p3)
    print("\ntest invalid...\n ")
    test_watering_system(p1, p4, p3)

    print("\n==end of program ==")
    '''
    try:
        water_plant(p1.name)
    except GardenError as e:
        print(f"garden error:\n{e}")
    try:
        water_plant(p2.name)
    except GardenError as e:
        print(f"garden error:\n{e}")
    try:
        water_plant(p3.name)
    except GardenError as e:
        print(f"garden error:\n{e}")
    '''
