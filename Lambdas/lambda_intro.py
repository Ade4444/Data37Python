def add_plus_one(num1, num2):
    return num1 + num2 + 1


print(add_plus_one(3, 7))

# Lambda (or anonymous) functions

addition = lambda num1, num2: num1 + num2 + 1

print(addition(5, 8))

# map

savings = [234.00, 555.00, 647.25, 839.00]

# bonus = savings with 10% added on

bonus = []

for saving in savings:
    bonus.append(saving * 1.1)
print(bonus)

def apply_bonus(saving):
    return saving * 1.1


bonus_map = list(map(apply_bonus, savings))
print(bonus_map)

bonus_lambda = list(map(lambda x: x * 1.1, savings))
print(bonus_lambda)

squared_bonus = list(map(lambda x: x ** 2, bonus_lambda))
print(squared_bonus)

print(list(f"{sb:.2f}" for sb in squared_bonus))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# use map and lambda to create a list of each number squared plus 3

square_plus_three = map(lambda n: n ** 2 + 3, numbers)    #print(square_plus_one)



# print(next(square_plus_three))
# print(next(square_plus_three))
# print(list(square_plus_three))

evens = filter(lambda x: x % 2 == 0, square_plus_three)

print(list(evens))

jobs = ["Data Analysts", "C# Developer", "Data Engineer", "Devops Engineer", "Data Architect"]

# Using map and filter with lambdas Produce a list of the data-based roles without the word data in there
# i.e. ["Analyst", "Engineer", "Architect"]

result = filter(lambda x: "Data" in x, jobs)
#print(list(result))

result1 = map(lambda x: x[5:], result)

print(list(result1))