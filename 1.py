"""
Напишите функцию для транспонирования матрицы
"""

matrix = [[1, 2, 4], [31, 17, 15]]


def transpose_matrix(matrix):
    """
    Transposes the matrix
    :param matrix: nested lists
    :return: nested lists
    """
    result = [list(row) for row in zip(*matrix)]
    return result


print(transpose_matrix(matrix))
