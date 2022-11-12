# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".


# # неверный код, удаляет слова с подряд идущими "абв"

# with open('task1.txt', 'r', encoding="UTF-8") as file:
#     data = file.read()
#     print('Исходный текст:')
#     print()
#     print( data)
#     words = data.split(' ')
#     fragment = 'абв'
#     new_text = []
#     for word in words:
#         if fragment not in word:
#             new_text.append(word)

# print()
# print('Переработанный текст:')
# print()
# print(' '.join(new_text))


# код с семинара

text = input('Input string: ')

tmp = []

for word in text.split():
    w = word.lower()
    if not ('а' in w and 'б' in w and 'в' in w):
        tmp.append(w)

print(' '.join(tmp))
