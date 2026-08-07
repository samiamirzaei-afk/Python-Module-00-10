class Plant:
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float) -> None:
        self.name = name.capitalize()
        self.height = height
        self.old = old
        self.growth_multi = growth_multi

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.old} days old")

    def grow(self) -> None:
        self.height *= self.growth_multi

    def age(self) -> None:
        self.old += 1


if __name__ == "__main__":
    p1 = Plant("rosemary", 10.0, 5, 1.04)
    p2 = Plant("radis", 4.0, 3, 1.23)
    p3 = Plant("jalapeno", 40.0, 30, 1.12)

    start_height = p3.height
    print("=== Garden Plant Growth ===")
    for x in range(1, 7 + 1):
        print(f"=== Day{x} ===")
        p3.age()
        p3.grow()
        p3.show()
    print(f"=== Growth this week:{round(p3.height - start_height, 2)}cm ===")
