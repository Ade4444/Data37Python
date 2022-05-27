
def make_orders(order):
    with open("drinks_menu.txt") as drink_file:
        drinks_options = drink_file.readline().split('\n')

        if order in drinks_options:
            with open("drinks_ordered.txt", "a") as drink_ordered:
                if order in drinks_options:
                    drink_ordered.write(f"{order}\n")
                    print("Drink has been added to your drinks order")
                else:
                    print("This drink is unavailable")





make_orders("SuperMalt")