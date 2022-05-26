class Car:
    def __init__(self, year, make, colour, top_speed):
        self.year_model = year
        self.make = make
        self.colour = colour
        self.top_speed = top_speed
        self.speed = 0


    def accel(self, speed):
        self.speed += speed

car_a = Car('2001', "Toyota", 'Black', 100)
car_b = Car("2021", "BMW", "Gun Metal Grey", 180)

print(car_a.colour)
print(car_a.top_speed)
print(car_a.make)
print(car_b.make)


car_a.accel(50)


print("accelerated " + str(car_a.speed ) + " mph")
print("accelerated " + str(car_b.speed ) + " mph")
