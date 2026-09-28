class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        discount = self.price * 10 / 100
        return self.price - discount


class Electronics(Product):
    def get_discounted_price(self):
        discount = self.price * 20 / 100
        return self.price - discount


p1 = Product("Book", 1000)
p2 = Electronics("Mobile", 20000)

print("Product:", p1.name)
print("Price after 10% discount:", p1.get_discounted_price())

print("Electronics:", p2.name)
print("Price after 20% discount:", p2.get_discounted_price())