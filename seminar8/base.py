import os
import csv
import pandas
import logger
import ui

fieldnames = ['num_id', 'first_name', 'last_name',
              'birthday', 'department', 'position', 'phones']


def show_directory():
    if os.path.exists('directory.csv'):
        data = pandas.read_csv('directory.csv')
        print(data)
        result = f'Кол-во сотрудников: {len(data)}'
    else:
        result = "База данных не найдена! Создана новая база данных!"
        with open('directory.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    ui.print_data(result)
    logger.logging.info(
        f'Просмотр базы данных. Результат: {result}')


def add_contact():
    if os.path.exists('directory.csv'):
        try:
            with open('directory.csv', 'r', encoding='UTF8') as csvfile:
                rows = (csv.reader(csvfile))
                max_id = 0
                next(rows)
                for row in rows:
                    if int(row[0]) > int(max_id):
                        max_id = row[0]
                num_id = int(max_id) + 1

        except Exception:
            result = "Ошибка при чтении файла!"
            ui.print_data(result)

    else:
        with open('directory.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        num_id = 1
        result = "База данных не найдена! Создана новая база данных!"
        ui.print_data(result)

    first_name = input('Укажите имя: ')
    last_name = input('Укажите фамилию: ')
    birthday = input('Укажите день рождения (ДД.ММ.ГГГГ): ')
    department = input('Укажите подразделение: ')
    position = input('Укажите должность: ')
    phones = input('Укажите номер(а) для связи: ')

    if confirm('Сохранить данные о сотруднике?'):
        with open('directory.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'num_id': num_id, 'first_name': first_name,
                            'last_name': last_name, 'birthday': birthday, 'department': department, 'position': position, 'phones': phones})
        result = f'Добавлен новый сотрудник: {first_name} {last_name}'
        ui.print_data(result)
        logger.logging.info(
            f'Добавление нового сотрудника. Результат: {result}')


def simple_search():
    count = 0
    search_str = input('Введите данные для поиска сотрудника: ')
    with open('directory.csv', encoding='utf-8') as csvfile:
        for line in csvfile:
            if search_str in line:
                print(line, end='')
                count += 1
        result = f'Кол-во найденных сотрудников: {count}.'
        ui.print_data(result)
    if count == 0:
        result = 'Данные не найдены!'
        ui.print_data(result)
    logger.logging.info(
        f'Простой поиск по базе данных. Результат: {result}')


def get_id():
    input_id = input('Введите id сотрудника: ')
    while not all(ch.isdigit() for ch in input_id):
        input_id = input('id должен быть положительным целым числом: ')
    return input_id


def id_search(id_):
    with open('directory.csv', 'r', encoding='UTF8') as csvfile:
        rows = (csv.reader(csvfile))
        for row in rows:
            if row[0] == id_:
                res = row
                return res


def confirm(text: str) -> bool:
    reply = input(f'{text} ("д", если да; любой другой ввод, если нет): ')
    return reply.lower() == 'д'


def delete_worker(id_):
    with open('directory.csv', 'r', encoding='UTF8') as csvfile:
        rows = (csv.reader(csvfile))
        temp = []
        for row in rows:
            if row[0] != id_:
                temp.append(row)
        with open('directory.csv', 'w', encoding='UTF8') as csvfile:
            for row in temp:
                csvfile.write(','.join(row))
                csvfile.write('\n')


def get_file_name() -> str:
    file_name = ''
    while not file_name:
        print('Для возврата в меню введите любые данные.')
        file_name = input('Введите имя файла: ')
    return file_name



