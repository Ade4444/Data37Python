

play = True
while play:
    x = int(input("Select a number you would like to play with?:\n "))
    for i in range(1, x + 1):

        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

    play_again = input("Would you like to play again?, Y to play again, or N to end\n").lower()
    if play_again == "n":
        play = False


