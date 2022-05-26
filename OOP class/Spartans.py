# class Spartan:                    # Class definition
#     def __init__(self, name, sex):         # initialise
#         sex = "F"
#         self.name = name
#         self.sex= "F"
#
# #    animal_type = "canine"      # Class Variable
#
#     def sex(self):             # method
#         return f"Damn! I am a {self.sex}"
#
# fido = Dog("Behzad", "M")
# print(fido.sex)
# print(fido.name)
# print(fido)


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

class Spartan:
    def __init__(self, name, stream, course, client):
        self.name = name
        self.stream = stream
        self.course = course
        self.client = client

david = Spartan(
    name = "David",
    course = "Data 37",
    stream = "Data Engineering"
)

