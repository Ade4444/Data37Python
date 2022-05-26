class Dog:                    # Class definition
    def __init__(self, name, colour):         # initialise
        animal_type = "canine"
        self.legs = 4
        self.name = name
        self.colour = colour

#    animal_type = "canine"      # Class Variable

    def bark(self):             # method
        return f"Woof! I am a {self.animal_type}"

fido = Dog("fido", "Black")


# fido = Dog()            # instance of class
# print(fido.animal_type)
# print(fido.bark())
#
# lassie = Dog()
# print(lassie.animal_type)
# print(lassie.bark())
#
#
#
# print(type(fido))
#
# Dog.animal_type = "arachnid"
# Dog.legs = 8
#
# print(fido.legs)
# print(fido.animal_type)
# print(lassie.animal_type)
# print(fido.bark())
#
# fido.legs = 3
# print(fido.legs)
# print(lassie.animal_type)
#
