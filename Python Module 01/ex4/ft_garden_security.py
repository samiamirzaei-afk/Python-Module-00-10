class Plant:
    def __init__(self, name: str, height: float, old: int,
                 growth_multi: float) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._old = 0
        self.set_height(height)
        self.set_age(old)
        self._growth_multi = growth_multi

    def get_age(self) -> int:
        pub_old = self._old
        return(pub_old)

    def set_age(self, num: int) -> None:
        if(num < 0):
            print(f"{self._name}: Negative age Error")
            print("*Age update rejected")
            return
        self._old = num
        print("Age updated to %d days old" % (self._old))

    def get_height(self) -> float:
        pub_height = self._height
        return(pub_height)

    def set_height(self, num: float) -> None:
        if(num < 0):
            print(f"{self._name}: Negative height Error")
            print("*Height update rejected")
            return
        self._height = num
        print("Height updated to %.2fcm" % (self._height))

    def show(self) -> None:
        print("%s: %.2fcm, %d days old" % (
           self._name, self._height, self._old))

    def grow(self) -> None:
        self._height *= self._growth_multi

    def age(self) -> None:
        self._old += 1
# name: str, height: float-cm, old: int-days, growth_multi : float) -> None:


if __name__ == "__main__":
    p1 = Plant("rosemary", 10.0, 5, 1.04)

    print("\n\nPlant created: %s: %.2fcm %d days old\n" % (
        p1._name, p1._height, p1._old))
    p1.set_height(20)
    p1.set_age(20)
    print("")
    p1.set_age(-5)
    p1.set_height(-5)
    print("")

    print("Current state: %s: %.2fcm %d days old" % (
        p1._name, p1._height, p1._old))
