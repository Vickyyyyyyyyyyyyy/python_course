import pandas as pd
import numpy as np

# Создание DataFrame с рандомными числами от 1 до 100 размером 10x10
data = np.random.randint(1, 101, size=(10, 10))
df = pd.DataFrame(data, columns=[chr(65 + i) for i in range(10)], index=[chr(97 + i) for i in range(10)])

# Вывод размерности матрицы
print("Размерность матрицы:")
print(df.shape)

# Вывод индексов столбцов
print("\nИндексы столбцов:")
print(df.columns)

# Вывод среднего значения всех чисел матрицы
print("\nСреднее значение всех чисел матрицы:")
print(df.mean().mean())

# Запись матрицы в CSV файл
df.to_csv('matrix.csv', index_label='Index')

# Вывод DataFrame
print("\nDataFrame:")
print(df)
