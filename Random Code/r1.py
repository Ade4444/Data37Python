class Dog:  # Class definition
    animal_type = "canine"
    legs = 4


def bark(self):  # method
    return f"Woof! I am a {self.animal_type}"


fido = Dog()  # instance of class
print(fido.animal_type)

lassie = Dog()
print(lassie.animal_type)

Dog.animal_type = "arachnid"
Dog.legs = 8

print(fido.legs)
print(fido.animal_type)
print(lassie.animal_type)
print(lassie.legs)
