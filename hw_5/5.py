import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла emojis.csv
df = pd.read_csv('emojis.csv')

# Преобразование столбца Date в тип datetime
df['Year'] = pd.to_datetime(df['Year'])


# Получение количества созданных эмоджи за каждый год
emojis_per_year = df.groupby('Year').size()

# Построение графика
emojis_per_year.plot(kind='bar', xlabel='Год', ylabel='Количество эмоджи', title='Количество эмоджи по годам')
plt.show()

