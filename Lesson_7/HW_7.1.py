"""
Task 7.1
"""
class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        for row in self.matrix_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for x in range(len(self.matrix_list)):
            for y in range (len(other.matrix_list)):
                self.matrix_list[x][y] = self.matrix_list[x][y] + other.matrix_list[x][y]
        return Matrix.__str__(self)

m_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m_2 = Matrix([[-3, -5, -32], [-2, -4, -6], [1, -64, 8]])
print(m_1.__add__(m_2))