class Plant:
    def __init__(self, name: str, height: float, age: int, growth_multi : float) -> None:
        self.name = name
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.growth_multi = growth_multi


    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height *= self.growth_multi

    def age(self, time: int) -> None:
        for x in rage(1, time):
            self.age += 1
            grow()
            



if __name__ == "__main__":
    p1 = Plant("rosemary", 10.0, 5, 1.04 )
    p2 = Plant("radis", 4.0, 3, 1.23)
    p3 = Plant("jalapeno", 40.0, 30, 1.12)

    p1.show()
    p2.show()
    p3.show()
