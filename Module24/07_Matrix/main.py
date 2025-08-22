import operator


class Matrix:
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.data = [[0 for _ in range(self.columns)] for _ in range(self.lines)]

    def output(self):
        for line in self.data:
            print('{:<5}'.format(' '.join(map(str, line))))

    def calculation(self, other, operation):
        if self.lines != other.lines or self.columns != other.columns:
            raise ValueError('Размеры матриц не совпадают.')

        result = Matrix(self.lines, self.columns)
        for i in range(self.lines):
            for j in range(self.columns):
                result.data[i][j] = operation(self.data[i][j], other.data[i][j])
        return result

    def multiply(self, other):
        if self.columns != other.lines:
            raise ValueError('Количество столбцов в первой матрице должно совпадать с количеством строк во второй.')

        result = Matrix(self.lines, other.columns)
        for i in range(self.lines):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def transpose(self):
        result = Matrix(self.columns, self.lines)
        for i in range(self.lines):
            for j in range(self.columns):
                result.data[j][i] = self.data[i][j]
        return result


# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
m1.output()

print("Матрица 2:")
m2.output()

print("Сложение матриц:")
result_addition = m1.calculation(m2, operator.add)
result_addition.output()

print("Вычитание матриц:")
result_subtraction = m1.calculation(m2, operator.sub)
result_subtraction.output()

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
result_multiplication = m1.multiply(m3)
result_multiplication.output()

print("Транспонирование матрицы 1:")
result_transpose = m1.transpose()
result_transpose.output()
