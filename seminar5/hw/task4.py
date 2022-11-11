# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('task4.txt', 'r', encoding="UTF-8") as file:
    string = file.readline()
    print('Исходные данные:', string)


def encode(decod):
    encod = ''
    count = 1
    char = decod[0]
    for i in range(1, len(decod)):
        if decod[i] == char:
            count += 1
        else:
            encod = encod + str(count) + char
            char = decod[i]
            count = 1
            encod = encod + str(count) + char
    return encod


def decode(encod):
    decod = ''
    char_amount = ''
    for i in range(len(encod)):
        if encod[i].isdigit():
            char_amount += encod[i]
        else:
            decod += encod[i] * int(char_amount)
        char_amount = ''
    print(decod)

    return decod


with open('task4.txt', 'r') as file:
    decod = file.read()

with open('task4res.txt', 'w') as file:
    encod = encode(decod)
    file.write(encod)

print('Результат кодирования: \t' + encode(decod))
