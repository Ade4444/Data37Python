# LEGB
# local, Enclosed, Global, Built-in

x = 10
#
# l = lambda x: x * 2
#
# print(l(2))
# print(x*2)


# def outer(x):
#     def inner():
#         x = 5
#         print(x)
#     inner()
# outer("Hello")
#
# def fizzbuzz():
#     while True:
#         n = input("End Number\n")
#         if n.isdigit():
#             n = int(n)
#             break
#
#     def fizzbuzz(num):
#


glob = "This is the global scope"

def local_function():
    def inner_function():
        print(__name__)


def type(x):
    return "I dunno, prob a string"

#local_function()
print(type(10)
