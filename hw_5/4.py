import pandas as pd

# Загрузка данных из файла emojis.csv
df = pd.read_csv('emojis.csv')

# Сортировка DataFrame по столбцу Rank в порядке убывания
df_sorted = df.sort_values(by='Rank', ascending=True)

# Вывод самой популярной подкатегории эмоджи
most_popular_category = df_sorted.iloc[0]['Subcategory']
print(f"Самая популярная подкатегория эмоджи: {most_popular_category}")
