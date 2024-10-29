class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_in_stock(self, quantity):
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        if self.is_in_stock(quantity):
            self.stock -= quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.is_in_stock(quantity):
            self.items.append((product, quantity))
        else:
            print(f"Not enough stock for {product.name}")

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items)

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart()

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

    def checkout(self):
        if self.cart.items:
            print(f"Total: ${self.cart.total_price()}")
        else:
            print("Cart is empty.")

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def buy_now(self):
        for product, quantity in self.products:
            product.reduce_stock(quantity)
        print(f"Order placed by {self.customer.name} for {len(self.products)} items.")

# Example usage:
product1 = Product("Laptop", 500, 10)
customer1 = Customer("prince", "prince@example.com")
customer1.add_to_cart(product1, 2)
customer1.checkout()
order = Order(customer1, customer1.cart.items)
order.buy_now()

product2 = Product("car", 1000, 10)
customer2 = Customer("ayo", "prince@example.com")
customer2.add_to_cart(product1, 2)
customer2.checkout()
order = Order(customer2, customer2.cart.items)
order.buy_now()