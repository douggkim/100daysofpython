class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __int__(self):
        super().__int__()
    # Fish도 breathe 가능

    def breathe(self):
        super().breath()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


