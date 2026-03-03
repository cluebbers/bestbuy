# Best Buy

Simple CLI store simulation for managing products and orders.

## Functions

`main.py`

- `print_menu()`: Shows the CLI menu and returns user input.
- `list_products(best_buy)`: Prints all active products.
- `show_amount(best_buy)`: Prints total quantity in stock.
- `make_order(best_buy)`: Builds a shopping list and places an order.
- `exit_program()`: Exits the app.
- `start(best_buy)`: Main app loop and menu routing.
- `main()`: Creates sample products and starts the store app.

`products.py` (`Product`)

- `get_quantity()`: Returns current quantity.
- `set_quantity(quantity)`: Updates quantity and active status.
- `is_active()`: Returns whether product is active.
- `activate()` / `deactivate()`: Toggles active state.
- `show()`: Returns formatted product info.
- `buy(quantity)`: Buys quantity, updates stock, returns total price.

`store.py` (`Store`)

- `add_product(product)`: Adds a product to the store.
- `remove_product(product)`: Removes a product from the store list.
- `get_total_quantity()`: Returns total stock across products.
- `get_all_products()`: Returns only active products.
- `order(shopping_list)`: Processes order and returns total price.

## Run

```bash
cd Assessment/bestbuy
python main.py
```
