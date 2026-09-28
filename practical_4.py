class Ticket:
    def __init__(self, movie, price):
        self.movie = movie
        self.price = price

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):
    def get_final_price(self):
        return super().get_final_price() + 50


t1 = Ticket("Avengers", 200)
t2 = PremiumTicket("Avengers", 200)

print("Movie:", t1.movie)
print("Normal Ticket Price:", t1.get_final_price())

print("Movie:", t2.movie)
print("Premium Ticket Price:", t2.get_final_price())