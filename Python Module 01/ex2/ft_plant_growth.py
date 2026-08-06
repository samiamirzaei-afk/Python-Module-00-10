class Plant:
    def __init__(self, name: str, height: float, old: int, growth_multi : float) -> None:
        self.name = name.capitalize()
        self.height = height
        self.old = old
        self.growth_multi = growth_multi

# condition = 0: only plant info, 1: day 2: week
    def show(self, condition: int, date: int, result: float) -> None:
        if condition == 1:
            print(f"=== Day {date}===")
        if(condition != 2):
            print(f"{self.name}: {round(self.height, 2)}cm, {self.old} days old")
        if condition == 2:
            print(f"=== Growth this week:{round(result, 2)}cm ===")

    def grow(self) -> None:
        self.height *= self.growth_multi

    def age(self, time: int) -> None:
        old_hight = self.height;
        for x in range(1, time + 1):
            self.old += 1
            self.grow()
            self.show(1, x, 0)
        self.show(2, 0, (self.height - old_hight))

            



if __name__ == "__main__":
    p1 = Plant("rosemary", 10.0, 5, 1.04 )
    p2 = Plant("radis", 4.0, 3, 1.23)
    p3 = Plant("jalapeno", 40.0, 30, 1.12)

    print("=== Garden Plant Growth ===")
    p1.age(7)
    print("\n")
    p2.age(7)
    print("\n")
    p3.age(7)
