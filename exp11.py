class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            return False

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

    def calculate_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())

    def clear_cart(self):
        self.items = {}
        print("Cart has been cleared.")

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        if product.update_stock(quantity):
            self.cart.add_product(product, quantity)
            print(f"{quantity} x {product.name} added to cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def checkout(self):
        total_cost = self.cart.calculate_total()
        print(f"Total cost for {self.name}: Rs.{total_cost:.2f}")
        self.cart.clear_cart()

if __name__ == "__main__":
    # Creating products
    product1 = Product("Laptop", 50000, 10)
    product2 = Product("Mouse", 500, 50)
    product3 = Product("Baby Oil", 5000, 10)
    product4 = Product("Deez Nuts", 5000, 20)

    # Creating customer
    customer = Customer("Saish Jagtap")

    # Adding products to cart
    customer.add_to_cart(product1, 1)
    customer.add_to_cart(product2, 2)
    customer.add_to_cart(product3, 1)
    customer.add_to_cart(product4, 3)

    # Checkout
    customer.checkout()

       