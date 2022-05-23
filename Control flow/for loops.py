alphabet = ["A", "B", "C", "D", "E"]

for l in alphabet:
    print("The Next letter is:")
    print(l.lower())
    if l == "D":
        print("Oh No")
    else:
        print("Hooray")


l = alphabet[0]
print(l.lower())
l = alphabet[1]
print(l.lower())
l = alphabet[2]
print(l.lower())
l = alphabet[3]
print(l.lower())
l = alphabet[4]
print(l.lower())

nest = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

for sublist in nest:
    print(sublist)
    for number in sublist:
        print(number)


hi = "Hello World"

print(hi)
for c in hi:
    print(c)

movies = {
    "Batman" : "Action",
    "Shrek" : "Comedy",
    "Romeo and Juliet":"Romance",
    "Pinnochio": "Animation"

}

for d in movies:
    print(d)

for d in movies:
    print("Im a movie")

r = range(5)
print(r)

for i in range(5):
    print(r)

    print(f"This is a line number: {i + 1}")

for x in enumerate(movies):
    print(x)
