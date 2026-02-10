import sys

import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


def print_menu():
    """
    Prints the user menu
    """
    print("  Store Menu:")
    print("  ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

    user_choice = input("Please choose a number: ")
    return user_choice


def list_products():
    """
    lists all products in store
    """
    print("  ----------")
    for i, product in enumerate(best_buy.get_all_products(), 1):
        print(
            f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}"
        )
    print("  ----------\n")


def show_amount():
    """
    prints total amount of items in store
    """
    print(f"Total of {best_buy.get_total_quantity()} items in store\n")


def make_order():
    '''
    Places an order
    '''
    list_products()
    products = best_buy.get_all_products()
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    while True:

        user_product = input("Which product # do you want? ")
        user_amount = input("What amount do you want? ")

        if user_product == "" and user_amount == "":
            print("********")
            total_payment = best_buy.order(shopping_list=shopping_list)
            print(f"Order made! Total payment: ${total_payment}\n")
            break
        try:
            user_product = int(user_product)
            user_amount = int(user_amount)
        except Exception as e:
            print(f"Error: {e}")
            continue
        single_order = (products[user_product - 1], user_amount)
        shopping_list.append(single_order)
        print("Product added to list!\n")


def exit_program():
    """
    program exits
    """
    sys.exit()


def start(store):
    """prints the menu and returns the user choice

    Returns:
        string: use rinput choice
    """
    func_dict = {
        "1": list_products,
        "2": show_amount,
        "3": make_order,
        "4": exit_program,
    }

    while True:
        user_choice = print_menu()
        if user_choice in func_dict:
            func_dict[user_choice]()
        else:
            print("Invalid choice")
            continue


if __name__ == "__main__":
    start(best_buy)
