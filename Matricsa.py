class Matrix:
    def __init__(self, mat1, mat2):
        self.mat1 = mat1
        self.mat2 = mat2

    def summ(self):
        if len(self.mat1) != len(self.mat2) or any(len(row1) != len(row2) for row1, row2 in zip(self.mat1, self.mat2)):
            return "Error, matrices rows are not equal"
        i = 0
        n = 0
        matrix3 = [[0] * len(self.mat1[0]) for _ in range(len(self.mat1))]

        while i != len(self.mat1):
            while n != len(self.mat1):
                matrix3[i][n] = self.mat1[i][n] + self.mat2[i][n]
                n += 1
            i += 1
            n = 0
        return matrix3

    def minus(self):
        if len(self.mat1) != len(self.mat2) or any(len(row1) != len(row2) for row1, row2 in zip(self.mat1, self.mat2)):
            return "Error, matrices rows are not equal"
        i = 0
        n = 0
        matrix3 = [[0] * len(self.mat1[0]) for _ in range(len(self.mat1))]

        while i != len(self.mat1):
            while n != len(self.mat1):
                matrix3[i][n] = self.mat1[i][n] - self.mat2[i][n]
                n += 1
            i += 1
            n = 0
        return matrix3

    def multiply(self):
        m1 = len(self.mat1)
        m2 = len(self.mat2)
        j = len(self.mat2[0])
        matrix3 = [[0 for _ in range(j)] for _ in range(m1)]
        for i in range(m1):
            for n in range(j):
                matrix3[i][n] = sum(self.mat1[i][kk] * self.mat2[kk][n] for kk in range(m2))
        return matrix3

    def multiply_matrix_num(self, num):
        matrix3 = [[0] * len(self.mat1[0]) for _ in range(len(self.mat1))]

        for i in range(len(self.mat1)):
            for n in range(len(self.mat1)):
                matrix3[i][n] = self.mat1[i][n] * num
        return matrix3

    def multiply_matrix_vector(self, vector):
        matrix3 = [[0] for _ in range(len(self.mat1))]
        for i in range(len(self.mat1)):
            for n in range(len(self.mat1[0])):
                matrix3[i][0] += self.mat1[i][n] * vector[0][n]
        return matrix3


matrix1 = [
    [3, 5, 7],
    [2, -1, 0],
    [4, 3, 2]
]
matrix2 = [
    [1, 2, 4],
    [2, 3, -2],
    [-1, 0, 1]
]
vector = [
    [1, 2, 3]
]
mt = Matrix(matrix1, matrix2)
print(mt.summ())
print(mt.minus())
print(mt.multiply())
print(mt.multiply_matrix_num(5))
print(mt.multiply_matrix_vector(vector))
