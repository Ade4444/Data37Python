# print()
# input()
# type()
#
# DRY - dont repeat yourself

# def greeting(name):
#     print(f"Hello {name}!")
#
# # Call the function
# greeting("Konrad")
# greeting("Dan")
# greeting("Harry")
#
# def greeting(name="you!"):
#     return "Hello " + name
#     print("This will never run")
#
# result = greeting()
# result = greeting("Sam")
# print(result)
#
# def addition (int1, int2):
#     return int1 + int2 + 1
#
# print(addition(4, 6))
#
#
# print("one", "two", 6345, {})
#
    # def multi_args(*args):
    #        print(args)
    #
    # multi_args(1, 2, 3)
#
# for arg in args:
#     print(arg)

# multi_args(1, 2, 3)

# def products(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
# print(products(4, 5, 6, 2))

# print(products())
#
# def products(*nums):
#     if len(nums) == 0:
#         return None
#
#     result = 1
#     for num in nums:
#         result *= num
#     return result
# print(products(4, 5, 6))
#
# print(products())
#
# def kwargs_demo(**kwargs): # key word arguements
#     print(kwargs, type(kwargs))
#
# print(kwargs_demo(a="One", b="Two"))

# def calculate_tip(list_of_meals, total_cost, tip_pc):
#     print("You had:")
#
#     for meal in list_of_meals:
#         print(f" - {meal}")
#     print(f"Your total is £{total_cost:.2f}")
#     print(f"With a {tip_pc:.0%} tip, the total is £{total_cost * (1 + tip_pc):.2f}")
#
# calculate_tip(["Burger", "Pizza"], 18.50, 0.1)
#
# def calculate_total_cost(**meal_prices):
#    # print(meal_prices, type(meal_prices))
#
#    return sum(meal_prices.values())
#
# print(calculate_total_cost(
#     Pizza=8.50,
#     Burger=9.00,
#     Hot_Dog=9.20
# ))

# def greeting(name: str):
#     print("Hello " + name)
#
# greeting("Dave")
#
# def division(denom: int, num: int) -> float:
#     return denom / num
#
# a = division(12, 6)
# a = division(12, 6)
#
# print(a)

# good functions

# Name them clearly, lowercase_with_underscores
# clear arguement names
# Functions that dont return something return None
# Keep them small
# use comments
# consider type hints

def fizzbuzz(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)

def fizzbuzz_game():
    for i in range(1, 101):
        print(fizzbuzz(i))

fizzbuzz_game()