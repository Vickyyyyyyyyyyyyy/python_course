import pandas as pd
import numpy as np

#1

# Создание DataFrame с рандомными целыми числами от 1 до 10
df = pd.DataFrame(np.random.randint(1, 11, size=(10, 10)))

# Вывод DataFrame
print(df)




