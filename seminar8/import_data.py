import os
import csv

fieldnames = ['num_id', 'first_name', 'last_name',
              'birthday', 'department', 'position', 'phones']

def upload_data(file_name: str) -> str:
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
            return "Ошибка при чтении directory.csv!"

    else:
        with open('directory.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        num_id = 1
        return "База данных не найдена! Создана новая база данных!"

    try:
        if not file_name[-4:] == '.csv':
            return 'Импортировать данные можно только из файлов CSV'
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile)
            next(rows)
            for row in rows:
                first_name = row[1]
                last_name = row[2]
                birthday = row[3]
                department = row[4]
                position = row[5]
                phones = row[6]
                with open('directory.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'num_id': num_id, 'first_name': first_name,
                                    'last_name': last_name, 'birthday': birthday,
                                     'department': department, 'position': position, 'phones': phones})
                num_id += 1
                print(f'Добавлен новый сотрудник: {first_name} {last_name}')
        return f'Данные из файла {file_name} успешно загружены!'
    except Exception:
        return f'Ошибка при чтении {file_name}!'