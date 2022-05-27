# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("File has not been found")
#     print(errmsg)
#     raise
#
#
# print(file, type(file))
# orders = list(map(lambda x: x.strip("\n"), file.readlines()))
# print(orders)
#
#
#
# file.close()




with open("order.txt") as file:
    orders = file.read().split("\n")

print(orders, type(orders))
orders_list = orders.split("\n")
print(orders_list)

print(orders)
print(file)
# colours = ["red\n", "yellow\n", "green\n", "blue\n"]
#
# with open("order.txt", "a") as file:
#     file.write("This will write\n")
#     file.writelines(colours)
