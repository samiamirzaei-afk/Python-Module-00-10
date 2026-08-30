class Plant:
    class Stats:
        def __init__(self) -> None:
            self.__show_count = 0
            self.__age_count = 0
            self.__grow_count = 0

        def show_stats(self) -> None:
            print(
                "Stats: %d grow, %d age, %d show"
                % (self.__grow_count, self.__age_count, self.__show_count)
            )

        def grow_call(self) -> None:
            self.__grow_count += 1

        def show_call(self) -> None:
            self.__show_count += 1

        def age_call(self) -> None:
            self.__age_count += 1

    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._old = 0
        self.set_height_start(height)
        self.set_age_start(old)
        self._growth_multi = growth_multi
        self.stats = Plant.Stats()

    def get_age(self) -> int:
        pub_old = self._old
        return pub_old

    def set_age(self, num: int) -> None:
        if num < 0:
            print(f"{self._name}: Error, age can not be a negative")
            print("Age updated rejected")
            return
        self._old = num
        print("Age updated to %d days old" % (self._old))

    def set_age_start(self, num: int) -> None:
        if num < 0:
            print(f"{self._name}: Error, age can not be a negative")
            print("Age updated rejected")
            return
        self._old = num

    def get_height(self) -> float:
        pub_height = self._height
        return pub_height

    def set_height(self, num: float) -> None:
        if num < 0:
            print(f"{self._name}: Error, height can not be a negative")
            print("height updated rejected")
            return
        self._height = num
        print("Height updated to %.2fcm" % (self._height))

    def set_height_start(self, num: float) -> None:
        if num < 0:
            print(f"{self._name}: Error, height can not be a negative")
            print("height updated rejected")
            return
        self._height = num

    def show(self) -> None:
        print("%s: %.2fcm, %d days old" %
              (self._name, self._height, self._old))
        self.stats.show_call()

    def grow(self) -> None:
        self._height *= self._growth_multi
        self.stats.grow_call()

    def age(self) -> None:
        self._old += 1
        self.stats.age_call()

    @staticmethod
    def is_year_older(num: int) -> bool:
        return num > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown", 0.0, 0, 1.0)


class Flower(Plant):
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float, color: str) -> None:
        super().__init__(name, height, old, growth_multi)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        if self._old < 20:
            print(
                "%s is too young to bloom!, needs %d days"
                % (self._name, 20 - self._old)
            )
        else:
            self._bloom = True
            print("%s is blooming %s" % (self._name, self._color))

    def show(self) -> None:
        super().show()
        print("Color: %s" % (self._color))
        print("Blooming: true" if self._bloom else "Blooming: false")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        old: int,
        growth_multi: float,
        color: str,
        seed_count: int,
    ) -> None:
        super().__init__(name, height, old, growth_multi, color)
        self._seed_count = seed_count

    def bloom(self) -> None:
        super().bloom()
        if self._bloom:
            print("%s produced %d seeds!" % (self._name, self._seed_count))
        else:
            print("%s has no seeds yet" % (self._name))

    def show(self) -> None:
        super().show()
        if self._bloom:
            print("Produced %d seeds" % (self._seed_count))
        else:
            print("No seeds yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_count = 0

        def shade_call(self) -> None:
            self.__shade_count += 1

        def show_stats(self) -> None:
            super().show_stats
            print("shade: %d" % (self.__shade_count))

    def __init__(
        self,
        name: str,
        height: float,
        old: int,
        growth_multi: float,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, old, growth_multi)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.Stats = self.Stats()

    def show(self) -> None:
        super().show()
        print("Trunk diameter: %.2fcm" % (self.trunk_diameter))

    def produce_shade(self) -> None:
        print(
            "%s creates a shadow of %.2fcm², (h:%.2f, w:%.2f)"
            % (
                self._name,
                (self._height * self.trunk_diameter),
                self._height,
                self.trunk_diameter,
            )
        )
        self.stats.shade_call()

    def grow(self) -> None:
        super().grow()
        self.trunk_diameter += 0.4


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        old: int,
        growth_multi: float,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, old, growth_multi)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print("Harevest season: %s" % (self._harvest_season))
        print("Nutritional value: %d" % (self._nutritional_value))

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1


def display_stat(plant: Plant) -> None:
    plant.stats.show_stats()


# name: str, height: float-cm, old: int-days, growth_multi : float) -> None:
if __name__ == "__main__":
    p1 = Flower("rosemary", 10.0, 19, 1.04, "purple")
    p2 = Tree("dark Oak", 40.5, 85, 1.11, 2.22)
    p3 = Vegetable("tomato", 20.5, 85, 1.14, "Summer")
    p4 = Seed("tomato seeds", 20.5, 19, 1.14, "red", 100)

    print("== Flower")
    p1.show()
    p1.bloom()
    p1.age()
    p1.bloom()
    p1.show()

    print("\n\n==Tree")
    p2.show()
    print()
    for x in range(0, 2):
        p2.grow()
        p2.produce_shade()
        p2.show()
        print("")

    print("\n\n==Vegetable")
    p3.show()
    print()
    for x in range(0, 5):
        p3.grow()
        p3.age()
        p3.show()
        print()

    print("\n\n==seed")
    p4.show()
    p4.bloom()
    p4.age()
    p4.bloom()
    p4.show()

    """
    print("stats for %s" % (p1._name))
    p1.stats.show_stats()
    print("stats for %s" % (p2._name))
    p2.stats.show_stats()
    print("stats for %s" % (p3._name))
    p3.stats.show_stats()
    print("stats for %s" % (p4._name))
    p4.stats.show_stats()
    print("lol xd")
    """
    display_stat(p1)
    display_stat(p2)
    display_stat(p3)
    display_stat(p4)
