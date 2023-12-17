import sympy as sp

class Math:
    def __init__(self, lear_rate, num_iterat):
        self.lear_rate = lear_rate
        self.num_iterat = num_iterat
        self.x = sp.symbols('x')

    def pr_func(self, x):
        func = self.my_func(x)
        pr_func = sp.diff(func, self.x)
        return pr_func

    def my_func(self, x):
        return x**2 + 2*x + 1

    def gradient_reesh(self):
        x = 0
        for _ in range(self.num_iterat):
            gradient = self.pr_func(x)
            x = x - self.lear_rate * gradient
        return x, self.my_func(x)

learning_rate = 0.1
num_iterations = 1000
mt = Math(learning_rate, num_iterations)
min_point, min_value = mt.gradient_reesh()
print(f"Минимум функции находится в точке {min_point} со значением {min_value}")
