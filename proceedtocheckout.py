class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.total = 0.0

    def add_item(self, item_name, price):
        self.cart.append({"item": item_name, "price": price})
        self.total += price
        print(f"Added {item_name} to cart for ${price:.2f}.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for item in self.cart:
                print(f"- {item['item']}: ${item['price']:.2f}")
            print(f"Total: ${self.total:.2f}")

    def proceed_to_checkout(self):
        if not self.cart:
            print("Your cart is empty. Add items before proceeding to checkout.")
        else:
            print("Proceeding to checkout...")
            print(f"Your total is ${self.total:.2f}. Thank you for shopping with us!")

# Example usage
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Headphones", 49.99)
cart.view_cart()
cart.proceed_to_checkout()