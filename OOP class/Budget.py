    # Create a Budget class that can keep track of different budget categories like food, clothing, and entertainment.
    # These should allow for depositing and withdrawing funds from each category, as well computing
    # category balances and transferring balance amounts between categories

class Budget:
    def __init__(self, acc_name):
        self.acc_name = acc_name
        self.total = 1000

    def deposit(self, amount):
        self.total += amount

    def withdraw(self, amount):
        self.total -= amount

    def balance(self):
        return self.total

    def transfer(self):
        pass

    def check_funds(self):
        pass

food_ = Budget("Food")
(food_.deposit(0))
(food_.withdraw(50))
print(food_.balance())
print(food_.acc_name)

cloth_ = Budget("clothing")
(cloth_.deposit(0))
(cloth_.withdraw(45))
print(cloth_.balance())
print(cloth_.acc_name)

ent_ = Budget("entertainment")
(ent_.deposit(0))
(ent_.withdraw(40))
print(ent_.balance())
print(ent_.acc_name)