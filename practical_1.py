class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        discount = self.price * 10 / 100
        return self.price - discount


p1 = Product("Laptop", 50000)

print("Product Name:", p1.name)
print("Original Price:", p1.price)
print("Discounted Price:", p1.get_discounted_price())