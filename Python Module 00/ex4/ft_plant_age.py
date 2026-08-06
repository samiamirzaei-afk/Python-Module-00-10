def ft_plant_age() -> None:
    harvest_time = 60
    age = int(input("Enter plant age in days: "))
    if (age > harvest_time):
        print("Plant is ready for harvest!")
        return None
    print("Plant needs more time")
