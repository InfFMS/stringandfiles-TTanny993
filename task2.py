# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
with open('task2.txt', 'r', encoding='utf-8') as f:
    t = f.read()
    updated = t.replace('Python', 'Питон')
    with open('task2_updated.txt', 'w', encoding='utf-8') as f_updated:
        f_updated.write(updated)
