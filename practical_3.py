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


def show_final_price(item):
    print("Name:", item.name)
    print("Final Price:", item.get_discounted_price())


p1 = Product("Book", 1000)
p2 = Electronics("Mobile", 20000)

show_final_price(p1)
show_final_price(p2)