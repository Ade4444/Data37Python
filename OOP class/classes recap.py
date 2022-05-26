class Bird:
    def __init__(self, species, colour):
        self.species = species
        self.colour = colour
        self.wings = 2
        self.can_fly = True
        self._age = 0

    def reproduce(self):
        if self._age < 2:
            return "Too Young"
        else:
            return "Egg"

    def age_up(self, years=1):
        self._age += years

    def get_age(self):
        return self._age
# instantiate an object

bird = Bird("Sparrow", "Brown")

bird.age_up()
bird.age_up()
bird.age_up()
egg = bird.reproduce()

bird._age = 1865
print(bird._age)

class Penguin(Bird):
    def __init__(self, subspecies, life_span, colour=("Black", "White")):
        super().__init__("Penguin", colour)
        self.subspecies = subspecies
        self.lifespan = life_span


    def hunt_for_fish(self):
        print("Splash")


penguin = Penguin("Rock Hopper", "15-20 years")
print(penguin.get_age())
print(penguin.can_fly)
print(penguin.colour)


penguin = Penguin("Gentoo", "13-15 years")
print(penguin.get_age())
print(penguin.can_fly)
print(penguin.colour)

class EmporerPenguin(Penguin):
    def __init__(self, lifespan, colour=("Black", "White")):
        super().__init__("Penguin", lifespan, colour)


print(penguin.lifespan)




