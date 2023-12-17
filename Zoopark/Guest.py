class Guest():
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def come_in(self):
        print(f"{self.name} зашел в ресторан")

    def take_order(self):
        print(f"{self.name} делает заказ")

