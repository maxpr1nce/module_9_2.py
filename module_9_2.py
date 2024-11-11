first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, длина которых не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Список пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Словарь строк и их длины с чётной длиной строк
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример результата выполнения программы
print(first_result)    # [8, 8, 9]
print(second_result)   # [('Elon', 'Task'), ('Musk', 'Task'), ('Musk', 'Git'), ('Programmer', 'Computer')]
print(third_result)    # {'Elon': 4, 'Task': 4, 'Musk': 4, 'Git': 3, 'Java': 4, 'Computer': 8, 'Assembler': 9}