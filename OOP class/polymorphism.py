class Mammal:
    def __init__(self, name):
        self.name = name

    def give_birth(self):
        print("Giving birth to live young")


class Platypus(Mammal):
    def __init__(self):
        super().__init__("platypus")

    def give_birth(self): #Overriding
        print("Laying Eggs..")

    def