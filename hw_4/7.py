import numpy as np


def neural_network_forward_propagation(A, S, last=False):
    A = np.ravel(A)  # Преобразование входного вектора в одномерный массив
    B = np.random.rand(S, len(A))

    result_matrix = np.dot(B, A)

    # Сумма каждой строки результирующей матрицы
    result_vector = np.sum(result_matrix)

    # Применение функции в зависимости от параметра last
    if not last:
        result_vector = np.sin(result_vector)
    else:
        result_vector = np.maximum(result_vector, 0)

    return result_vector, B


# Тестирование функции
vector1 = np.random.rand(5)
result1, matrix1 = neural_network_forward_propagation(vector1, 10)

result2, matrix2 = neural_network_forward_propagation(result1, 10)

result3, matrix3 = neural_network_forward_propagation(result2, 5, last=True)
result3_percentage = result3 * 100

# Вывод результатов
print("Результат 1:", result1)
print("Матрица 1:", matrix1)
print("Результат 2:", result2)
print("Матрица 2:", matrix2)
print("Результат 3 в процентах:", result3_percentage)
print("Матрица 3:", matrix3)
