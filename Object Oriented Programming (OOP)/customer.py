import person

class Customer(person.Person):
    def __init__(self, fname, lname, address):
        self.address = address
        super().__init__(fname, lname)

    def print(self):
        print(f"Address: {self.address}", end= "")
        super().print()

