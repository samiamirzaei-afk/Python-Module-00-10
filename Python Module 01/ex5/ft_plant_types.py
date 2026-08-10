class Plant:
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._old = 0
        self.set_height_start(height)
        self.set_age_start(old)
        self._growth_multi = growth_multi

    def get_age(self) -> int:
        pub_old = self._old
        return(pub_old)

    def set_age(self, num: int) -> None:
        if(num < 0):
            print(f"{self._name}: Error, age can not be a negative")
            print("Age updated rejected")
            return
        self._old = num
        print("Age updated to %d days old" % (self._old))

    def set_age_start(self, num: int) -> None:
        if(num < 0):
            print(f"{self._name}: Error, age can not be a negative")
            print("Age updated rejected")
            return
        self._old = num

    def get_height(self) -> float:
        pub_height = self._height
        return(pub_height)

    def set_height(self, num: float) -> None:
        if(num < 0):
            print(f"{self._name}: Error, height can not be a negative")
            print("height updated rejected")
            return
        self._height = num
        print("Height updated to %.2fcm" % (self._height))

    def set_height_start(self, num: float) -> None:
        if(num < 0):
            print(f"{self._name}: Error, height can not be a negative")
            print("height updated rejected")
            return
        self._height = num

    def show(self) -> None:
        print("%s: %.2fcm, %d days old" % (
           self._name, self._height, self._old))

    def grow(self) -> None:
        self._height *= self._growth_multi

    def age(self) -> None:
        self._old += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float, color: str) -> None:
        super().__init__(name, height, old, growth_multi)
        self._color = color

    def bloom(self) -> None:
        if(self._old < 20):
            print("%s is too young to bloom!, needs %d days" % (
                self._name, 20 - self._old))
        else:
            print("%s is blooming %s" % (self._name, self._color))

    def show(self) -> None:
        super().show()
        print("Color: %s" % (self._color))


class Tree(Plant):
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float, trunk_diameter: float) -> None:
        super().__init__(name, height, old, growth_multi)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print("Trunk diameter: %.2fcm" % (self.trunk_diameter))

    def produce_shade(self):
        print("%s creates a shadow of %.2fcm², (h:%.2f, w:%.2f)" % (
            self._name, (self._height * self.trunk_diameter), self._height,
            self.trunk_diameter))

    def grow(self):
        super().grow()
        self.trunk_diameter += 0.4


class Vegetable(Plant):
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float, harvest_season: str) -> None:
        super().__init__(name, height, old, growth_multi)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print("Harevest season: %s)" % (self._harvest_season))
        print("Nutritional value: %d)" % (self._nutritional_value))

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


# name: str, height: float-cm, old: int-days, growth_multi : float) -> None:
if __name__ == "__main__":
    p1 = Flower("rosemary", 10.0, 5, 1.04, "purple")
    p2 = Tree("Oak", 40.5, 85, 1.11, 2.22)
    p3 = Vegetable("tomato", 20.5, 85, 1.14, "Summer")
    x = 1
#    for x in range(x , 30):
#        p2.grow()
#        p2.age
#        p2.produce_shade()
#        p2.show()
#        print()

    for x in range(x, 30):
        p3.grow()
        p3.age()
        p3.show()
        print()
