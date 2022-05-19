t = True
f = False
#print(t, type(t))
print(True and True)
print(True and False)
print(True or False)

match = "Target"
print(match == "Target")

he = "helloworld"
hi = "hello world"
ho = "HELLO WORLD"
print(he.isalpha()) # because of space, must be alphabet
print(hi.islower()) #if all are in lower case
print(ho.isupper()) # if all are in upper case
print(hi.endswith("d")) #entry required to say what it ends with
print(hi.startswith("h"))

print(ho.isupper() and ho.startswith("HE"))

print(bool(1))
#print(int(bool))

print(bool(-18343))

print(bool("Soap"))

print(len("check how many letter"))

x = None

print(x is not None)

