# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".


with open('task1.txt', 'r', encoding="UTF-8") as file:
    data = file.read()
    print('Исходный текст:')
    print()
    print( data)
    words = data.split(' ')
    fragment = 'абв'
    new_text = []
    for word in words:
        if fragment not in word:
            new_text.append(word)
            
print()
print('Переработанный текст:')
print()
print(' '.join(new_text))
