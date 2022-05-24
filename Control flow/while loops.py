x = 0

while x <= 10:
    print(f"While loop running: {x}")
    if x == 5:
        print("Yay! 5!")
        break
    x += 1

 #   age = input("What is your age?\n")

   # if age > 15:
     #   print("you can see the film")

    keep_asking = True

    while keep_asking:
        age = input("What is your age?\n")
        if age.isdigit():
            age_int = int(age)
        else:
            print("Please enter a valid number in digits.")

        print(f"Your age is{age_int}")

