import os
import csv
import logger as log
# import re

fieldnames = ['num_id', 'first_name', 'last_name', 'birthday', 'job', 'phone']


def show_directory():
    if os.path.exists('directory.csv'):
        try:
            count = 0
            with open('directory.csv', newline='', encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)
                    count += 1
                print(f'Кол-во контактов: {count}')
        except Exception:
            print("Ошибка при чтении файла!")
    else:
        print("Справочник не найден! Создан новый справочник!")
        with open('directory.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


def add_contact():
    if os.path.exists('directory.csv'):
        try:
            count = 0
            with open('directory.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    count += 1
                num_id = count + 1
        except Exception:
            print("Ошибка при чтении файла!")

    else:
        with open('directory.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        num_id = 1
        print("Справочник не найден! Создан новый справочник!")

    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    birthday = input('Введите день рождения (ДД.ММ.ГГГГ): ')
    job = input('Введите место работы: ')
    phone = input('Введите номер телефона (через запятую, если несколько): ')

    with open('directory.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'num_id': num_id, 'first_name': first_name,
                        'last_name': last_name, 'birthday': birthday, 'job': job, 'phone': phone})
    print(f'Добавлен новый контакт: {first_name} {last_name}')


def simple_search():
    print('Чтобы точно получить определенный контакт - введите id контакта в формате "id N"')
    count = 0
    search_str = input('Введите данные для поиска контакта: ')
    with open('directory.csv', encoding='utf-8') as csvfile:
        for line in csvfile:
            if search_str in line:
                print(line, end='')
                count += 1
        print(f'Кол-во найденных контактов: {count}')
    if count == 0:
        print(f'Данные не найдены!.')


# # def delete_contact():
# #     print('Чтобы точно получить определенный контакт - введите id контакта в формате "id N"')
# #     count = 0
# #     search_str = input('Введите данные для поиска контакта: ')
# #     with open('directory.csv', 'r',encoding='utf-8') as data:


# # # def delete_contact(id_contact: str) -> str:
# #     with open('directory.csv', 'r', encoding='UTF8') as data:
# #         rows = list(csv.reader(data))
# #         contacts = []
# #         for row in rows:
# #             contact = {}
# #             if row[0] != id_contact:
# #                 for i in range(len(contact)):
# #                     contact[contact[i]] = row[i + 1]
# #                 contacts.append(contact)
# #             else:
# #                 name = row[1]

# #     # with open('directory.csv', 'w+', encoding='UTF8'):
# #     #     pass
# #     # # for contact in contacts:
# #     # #     add_contact(contact)
# #     # return f'Контакт "{name}" успешно удалён'

# # def enter_id() -> str:
# #     contact_id = ''
# #     while not contact_id:
# #         contact_id = input('Введите id контакта, который нужно удалить: ')
# #         while not all(ch.isdigit() for ch in contact_id):
# #             contact_id = input('id должен быть положительным целым числом: ')
# #     return contact_id

# # def id_search(contact_id: str) -> str or dict:
# def id_search():
#     contact_id = ''
#     while not contact_id:
#         contact_id = input('Введите id контакта: ')
#         while not all(ch.isdigit() for ch in contact_id):
#             contact_id = input('id должен быть натуральным числом: ')
#     # return contact_id
# # def id_search(contact_id: str) -> str or dict:
#     with open('directory.csv', newline='', encoding='utf-8') as csvfile:
#         rows = csv.reader(csvfile)
#         # rows = list(csvfile.read())
#         if len(rows) < int(contact_id):
#             return f'Контакт с id {contact_id} не найден'
#         contact = ''
#         for row in rows:
#     #if current rows 2nd value is equal to input, print that row
#             if contact_id == row[0]:
#                 rows.__next__()
#                 csvwriter.writerow(row)
#         # for row in rows:
#         #     if row[0] == contact_id:
#         #         # print(row[0])
#         #         for i in range(len(fieldnames)):
#         #             print(i)
#         #             print(len(fieldnames))
#         #             print(range(len(fieldnames)))
#         #             print(row[i])
#         #             print (row)
#         #             # print(contact[fieldnames[i]])
#         #             contact[fieldnames[i]] = row[i]
#         #             print(contact)
#         #         break
#         #     print(contact)
#         # # return contact
