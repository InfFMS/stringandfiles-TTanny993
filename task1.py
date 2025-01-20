# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open('task1.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
    lines = len(line)
    words = sum(len(line.split()) if '—' not in line else len(line.split()) - line.count('—') for line in line)
    chars = sum(len(line) for line in line)
    print(lines)
    print(words)
    print(chars)