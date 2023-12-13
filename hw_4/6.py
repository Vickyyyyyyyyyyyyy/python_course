#6

import re

class FileAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = None
        self.read_file()

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.file_data = file.readlines()
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    def search_text(self, pattern):
        if self.file_data is None:
            print("Файл не был прочитан.")
            return []

        matches = []
        for line_number, line in enumerate(self.file_data, start=1):
            found = re.findall(pattern, line)
            if found:
                matches.append({'line': line_number, 'text': line.strip(), 'matches': found})

        return matches

# Пример использования
file_path = 'example.txt'
analyzer = FileAnalyzer(file_path)

if analyzer.file_data:
    search_pattern = input("Введите паттерн поиска: ")
    results = analyzer.search_text(search_pattern)

    if results:
        print("Результаты поиска:")
        for result in results:
            print(f"Строка {result['line']}: {result['text']} - Найденные совпадения: {result['matches']}")
    else:
        print("Совпадений не найдено.")