# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.
n = int(input())
with open('task4.txt', 'w', encoding='utf-8') as f:
    for i in range(n):
        t = input()
        t = t.upper()
        t = t.replace(' ', '_')
        f.write(t)
        f.write('\n')
with open('task4.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)