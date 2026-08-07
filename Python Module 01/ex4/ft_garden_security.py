class Plant:
    def __init__(self, name: str, height: float, old: int,
                 growth_multi : float) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._old = 0
        self.set_height(height)
        self.set_age(old)
        self._growth_multi = growth_multi

    def get_age(self) -> int:
        pub_old = self._old 
        return(pub_old)

    def set_age(self, num: int) -> int:
        if(num < 0):
            print(f"{self._name}: Error, age can not be a negative")
            print(f"Age updated rejected")
            return
        self._old = num

    def get_height(self) -> int:
        pub_height = self._height
        return(pub_height)

    def set_height(self, num: float) -> int:
        if(num < 0):
            print(f"{self._name}: Error, height can not be a negative")
            print(f"height updated rejected")
            return
        self._height = num



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
    p2 = Plant("radis", 4.0, 3, 1.23)
    p3 = Plant("jalapeno", 40.0, 30, 1.12)
    p4 = Plant("barley ", 5.0, 7, 1.07)
    p5 = Plant("garlic", 3.0, 12, 1.02)
    
    p1.show()

    p1.set_age(-5)
    p1.set_age(20)
    p1.show()
    p1.set_height(-5)
    p1.set_height(20)
    p1.show()
