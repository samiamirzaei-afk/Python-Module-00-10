def ft_water_reminder() -> None:
    water_time = 2
    age = int(input("Days since last watering: "))
    if (age > water_time):
        print("Water the plants!")
        return None
    print("Plants are fine")
