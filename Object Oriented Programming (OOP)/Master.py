import customer
import employee
import random

if random.randint(0, 1) == 0:
    my_person = customer.Customer('Mike', 'Akin', 'London')

#cust = customer.Customer('Mike', 'Akin', 'London')
#cust.print()
#cust._lastName = "Smith"
# cust.first_name = "Samuel"
else:
    my_person = employee.Employee("Minato", "Fujiwara", "Finance")
#emp = employee.Employee("Minato", "Fujiwara", "Finance")
#emp.print()
my_person.print()