'''
Sometimes the built-in Python errors are not specific enough for your garden program.
You can create your own error types to make your code clearer and more helpful.
Create these simple custom exception classes:
• GardenError - A basic error for garden problems
• PlantError - For problems with plants (inherits from GardenError)
• WaterError - For problems with watering (inherits from GardenError)
Each custom exception should:
• Be a simple class that inherits from Exception (or GardenError)
• Have a specific default error message (e.g., “Unknown plant error”) if none is provided
Create functions that:
• Raise your custom errors in different situations
• Show how to catch your specific error types
• Demonstrate that catching GardenError catches all garden-related errors
'''

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        self.message = message
        super().__init__(self.message)


# --- Functions that raise the custom errors ---

def check_plant_health(plant_name: str, is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError(f"{plant_name} is wilting and needs attention")


def check_water_level(liters: float) -> None:
    if liters <= 0:
        raise WaterError("No water left in the watering can")
    if liters > 10:
        raise WaterError(f"{liters}L is too much water, you'll flood the bed")


def plant_unknown_species(species: str) -> None:
    # Using the default message, since we don't pass one in
    if species not in ("tomato", "basil", "carrot"):
        raise PlantError()


# --- Demonstrating catching specific error types ---

def demo_specific_catches() -> None:
    print("Testing check_plant_health:")
    try:
        check_plant_health("Rose", True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting check_water_level:")
    try:
        check_water_level(15)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting default message:")
    try:
        plant_unknown_species("cactus")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


# --- Demonstrating that GardenError catches everything ---

def demo_catch_all_garden_errors() -> None:
    situations = [
        lambda: check_plant_health("Fern", True),
        lambda: check_water_level(-1),
        lambda: plant_unknown_species("dragonfruit"),
    ]

    for situation in situations:
        try:
            situation()
        except GardenError as e:
            # This catches PlantError and WaterError too, since both inherit from GardenError
            print(f"Caught by GardenError handler: {type(e).__name__}: {e}")


if __name__ == "__main__":
    demo_specific_catches()
    print("\n" + "=" * 40 + "\n")
    demo_catch_all_garden_errors()
