# # birth_year = input("Enter your birth year: ")
# # age = 2022 - int(birth_year)
# # print(age)
#
# # def calc(n1, n2):
# n1 = input("pick your first number: ")
# n2 = input("pick your second number: ")
# total = float(n1) + float(n2)
# print(f"{n1} plus {n2} is equal to {total}")
#
# course = "Python for beginners"
#
# print(course.replace("for", "4"))
#
# temperature = 35
#
# if temperature > 30:
#     print("over room temp")
#
# else:
#     print("better go check out the thermostat")

#
# weight = float(input("What is you weight:\n"))
# unit = input("Kg ('K') or Lbs ('L') \n").upper()
#
# if unit == "K":
#     conv1 = weight / 0.45
#     print(f"your weight in Kg is {conv1}")
# elif unit == "L":
#     conv2 = weight * 0.45
#     print(f"your weight in Lbs is {conv2}")
#

# i = 1
# while i < 10:
#     print(i * 2)
#     i +=1
#
# #numbers = range(1, 17, 2)
# for num in range(17):
#     if num % 2 == 0:
#         print(num)

# def greet_user():
#     print("Hi there!")
#     print("Welcome abroad")
#
#
# print("Start")
# greet_user()
# print("Finish")
#
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)":"👍",
#         ":(": "🔥"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#         return output
#
#
# message = input(">")
# print(emoji_converter(message))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point = Point(10, 20)
# print(point.x)
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)
#
# point = Point()
# print(point.x)
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi I am {self.name}")
#
# john = Person("John Smith")
# john.talk()
#
# bob = Person("Bobby V")
# bob.talk()

# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
#
# class Cat(Mammal):
#     def be_annoy(self):
#         print("be annoying")
#
#
# dog1 = Dog()
# dog1.walk()
# dog1.bark()
# cat1 = Cat()
# cat1.be_annoy()

# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("config is", self.cpu, self.ram)
#
# comp1 = Computer("i5", "16GB")
# comp2 = Computer("i7", "32GB")
#
# comp1.config()
# comp2.config()

# class Students:
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):
#         return (self.m1+ self.m2 +self.m3)/3
#
# s1 = Students(34, 47, 32)
# s2 = Students(89, 32, 12)
#
# print(s1.avg())

# class A:
#     def __init__(self):
#         print("In A")
#
#     def feature1(self):
#         print("Feature One")
#
#     def feature2(self):
#         print("Feature Two")
#
#
# class B(A): # this helps to inherit from class A
#     def __init__(self):
#         super().__init__()
#         print("In B")
#
#     def feature3(self):
#         print("Feature Three")
#
#     def feature4(self):
#         print("Feature Four")
#
#
# a1 = A()
# b1 = B()
#
# b1.feature2()
# a1.feature2()

#
#class PyCharm:
#
#     def execute(self):
#         print("Compiling")
#         print("Running")
#
#
# class Editor:
#
#     def execute(self):
#         print("Compiling")
#         print("Running")
#         print("Spelling")
#         print("Converting")
#
# class Laptop:
#     def code(self, ide):
#         ide.execute()
#
# ide = PyCharm() # change to editor to print editor tasks
# lap1 = Laptop()
# lap1.code(ide)

