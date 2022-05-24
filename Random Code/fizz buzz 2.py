
i = int(input("Select a number you would like to play with?:\n "))

if i % 3 == 0 and i % 5 == 0:
    print("Fizzbuzz")

elif i % 3 == 0:
    print("Fizz")

elif i % 5 == 0:
    print("Buzz")

else:
    print(i)

