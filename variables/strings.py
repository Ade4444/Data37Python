h = "Hello World!"

double = "Double Quotes"
single = "Single Quotes"

print(double, single)

failure = "I said" "Oh no!"""
double_in_single = 'I said "Oh no"'

# both 'i said "Oh no!" David'\s

h = "hello world"

print(h[1])

print(h[6])

print(h[-1])

print(h[-3])

print(h[2:6]) #llo
print(h[3:8]) #lo wo

print(h[3:-3]) #lo wo

print(h[1:-1:3])
print(h[4::2])



# Methods

print(type(h))
print(h.lower())
print(h.upper())

print(h.capitalize())
print(h.strip("world"))
print(h.count('l', 1,10))
print(h.count('h'))
print(h.replace("o", "ooo"))

print(h.strip())
print(h.replace("o", "oooo").upper().count("O"))

ho = "hi. ho. hello"

s_list = ho.split(". ")
print(s_list)
#print(h.split(", "))

new_sentence = ". ".join(h.capitalize() for x in ho.split(". "))
print(new_sentence)

this_will_work = 6
print(this_will_work)

a = "Mr"
b = "Blue"
c = "Sky"

print(a + " " + b + " " + c)

h = "I. am. testing. splitting"

print(h.split(". "))

