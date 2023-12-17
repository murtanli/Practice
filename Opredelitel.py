import random
import numpy as np


class Matrica:
    def __init__(self, mat):
        self.mat = mat

    def opredelit(self):
        plus = minus = 1
        plus2 = minus2 = 1
        plus3 = minus3 = 1
        n = 0
        l = len(self.mat) - 1

        for i in range(len(self.mat)):
            plus *= self.mat[i][n]
            plus2 *= self.mat[i - 1][n]
            plus3 *= self.mat[i - 2][n]

            minus *= self.mat[i][l]
            minus2 *= self.mat[i - 1][l - 1]
            minus3 *= self.mat[i - 1][l]
            n += 1
            l -= 1

        return (plus + plus2 + plus3 - minus - minus2 - minus3)


n, m = map(int, input("Введите значения n и m через пробел: ").split())
if n != m or n > 3 and m > 3:
    print("error")
else:
    mat = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(m):
            mat[i][k] = random.randint(1, 30)
            # mat[i][k] = int(input(f"Enter num mas[{i} {k}]"))
    det = np.linalg.det(mat)
    otv = Matrica(mat).opredelit()
    print(f"currect answ {det} my answ {otv}")
