class Plant:
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float) -> None:
        self._name = name.capitalize()
        self._height = height
        self._old = old
        self._growth_multi = growth_multi

    def show(self) -> None:
        print("%s: %.2fcm, %d days old" % (
            self._name, self._height, self._old))
#  print(f"{self._name}: {round(self._height, 2)}cm, {self._old} days old")

    def grow(self) -> None:
        self._height *= self._growth_multi

    def age(self) -> None:
        self._old += 1


# name: str, height: float-cm, old: int-days, growth_multi : float) -> None:
if __name__ == "__main__":
    p1 = Plant("rosemary", 10.0, 5, 1.04)
    p2 = Plant("radis", 4.0, 3, 1.23)
    p3 = Plant("jalapeno", 40.0, 30, 1.12)
    p4 = Plant("barley ", 5.0, 7, 1.07)
    p5 = Plant("garlic", 3.0, 12, 1.02)

    p1.show()
