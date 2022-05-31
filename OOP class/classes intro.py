class Dog:  # Class definition
    def __init__(self, name, colour):  # initialise
        self.animal_type = "canine"
        self.legs = 4
        self.name = name
        self.colour = colour

    def bark(self):  # method
        return f"Woof! I am a {self.animal_type}"

fido = Dog("fido", "Black")
print(fido.animal_type)
print(fido.name)
print(fido.colour)
print(fido.bark())

lassie = Dog("lassie", "Brown")
print(lassie.animal_type)
print(lassie.name)
print(lassie.colour)
print(lassie.bark())


class Spartan:
    def __init__(self, name, stream, course, client):
        self.name = name
        self.stream = stream
        self.course = course
        self.client = client

david = Spartan("Dave", "Data Eng", "Data 37", "Home Office")

print(david.course)