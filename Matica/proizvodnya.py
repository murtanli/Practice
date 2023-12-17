import sympy as sp

class Math:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def pr(self):
        x = sp.symbols('x')
        y = self.a * x ** 2 + self.b * x + self.c
        y_prime = sp.diff(y, x)
        return ("Исходная функция:", y), ("Производная функции:", y_prime)

mt = Math(2, 4, 5)
print(mt.pr())
