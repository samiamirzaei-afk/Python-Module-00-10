class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p1 = Plant("rose", 10, 5)
    p2 = Plant("radis", 4, 3)
    p3 = Plant("Jalapeno", 40, 30)

    p1.show()
    p2.show()
    p3.show()
