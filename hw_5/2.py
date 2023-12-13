#2

import pandas as pd
import numpy as np

# Создание DataFrame с рандомными целыми числами от 1 до 10
data = np.random.randint(1, 11, size=(10, 10))
df = pd.DataFrame(data, columns=[f'Col{i}' for i in range(1, 11)], index=[chr(65 + i) for i in range(10)])

# Вывод DataFrame
print("DataFrame с индексами:")
print(df)

# Фильтрация строк, в которых все числа > 5
filtered_df = df[df > 5].dropna()

if not filtered_df.empty:
    # Преобразование чисел в строки и объединение в строку через пробел
    filtered_row = filtered_df.astype('int').astype(str).apply(' '.join, axis=1).iloc[0]
    print("\nСтрока, в которой все числа > 5:")
    print(filtered_row)
else:
    print("\nНет строк, в которых все числа > 5.")
