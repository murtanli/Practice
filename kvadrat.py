import cmath


class Form:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def kv(self, num, step):
        res = 1
        for i in range(step):
            res = res * num
        return res

    def found_kvadrat(self):
        delta = self.kv(self.b, 2) - 4 * self.a * self.c
        if delta > 0:
            root1 = (-self.b + cmath.sqrt(delta)) / (2 * self.a)
            root2 = (-self.b - cmath.sqrt(delta)) / (2 * self.a)
            return root1, root2
        elif delta == 0:
            root = -self.b / (2 * self.a)
            return root
        else:
            return "Корней нет"


fm = Form(1, 2, 10)
print(fm.found_kvadrat())
