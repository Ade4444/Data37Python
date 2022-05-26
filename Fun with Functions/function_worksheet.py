print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
def divisors(n):
    result = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result


print(divisors(44))

# A1a:


print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

def divis(a, b):
    if a % b == 0:
        print(True)
    else:
        print(False)


divis(9, 2)

# A1b:


# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")


# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
# "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def alpha_letter(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]

    return alphabet.index(letter)


def index_name(word):
    index = []
    for i in word:
        x = alpha_letter((i).lower())

        index.append(x + 1)
    return index


print(index_name("Ad"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

def alpha_letter(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]

    return str(alphabet.index(letter) + 1)


def index_name(word):
    index = []
    idNumber = ""
    for i in word:
        x = alpha_letter((i).lower())
        index.append(x)
        idNumber = "".join(index)
    return idNumber

print(index_name("Adeola"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

def alpha_letter(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]

    return str(alphabet.index(letter))


def index_name(word):
    index = []
    idNumber = ""
    for i in word:
        x = alpha_letter((i).lower())
        index.append(x)
        idNumber = "".join(index)
    return idNumber

def password(id):
    total = 0
    index_list = []
    for letter in id:
        pos = alpha_letter(letter)
        index_list.append(pos)
        total += pos

    max = int(index_name(id))
    password = max - total
    return password

print(password("ade"))
# A2c:


# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            return True


print(prime(3))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

def prime(x):
    if x.isnumeric():

        for i in range(2, x):
            if x % i == 0:
                return False
            else:
                return True


print(prime("Fo"))
# A3b:


# -------------------------------------------------------------------------------------- #
