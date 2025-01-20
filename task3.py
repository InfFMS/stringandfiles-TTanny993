# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
from string import punctuation

with open('task3.txt', 'r', encoding='utf-8') as f:
    t = f.read()
    t = t.replace('\n', ' ')
    t = t.replace('\t', ' ')
    for symbol in punctuation:
        t = t.replace(symbol, ' ')
    words = t.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    up = sorted(list(set(words)))
    with open('task3_update.txt', 'w', encoding='utf-8') as f_up:
        for word in up:
            count = words.count(word)
            f_up.write(f'{word}: {count}\n')