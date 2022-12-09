import os


def export_file():
    running = True
    while running:
        print('''
    1 - экспортировать базу данных в .html
    2 - экспортировать базу данных в .txt
    ''')
        user_choice = ''
        while not user_choice:
            user_choice = input('Выбирите действие: ')
            match user_choice:
                case '1':
                    if os.path.exists('directory.csv'):
                        try:
                            with open('directory.csv', newline='', encoding="utf-8") as csvfile:
                                reader = csvfile.readlines()
                                style = 'style = "font-size:20px;"'
                                html = '<html>\n <head></head>\n <body>\n'
                                for _ in reader:
                                    html += '     <p {}> {} </p>\n'.format(
                                        style, _)
                                with open('directory.html', 'w', encoding='utf-8') as data:
                                    data.write(html)
                                    result = "Файл сохранён как 'directory.html'"
                        except Exception:
                            result = "Ошибка при чтении или записи файла!"
                    else:
                        result = "База данных не найдена!"
                    return result
                case '2':
                    if os.path.exists('directory.csv'):
                        try:
                            with open('directory.csv', encoding='utf-8') as file:
                                data = file.read()
                            with open('directory.txt', 'w', encoding='utf-8') as file:
                                file.write(f'{data}\n')
                                result = "Файл сохранён как 'directory.txt'"
                        except Exception:
                            result = "Ошибка при чтении или записи файла!"
                    else:
                        result = "База данных не найдена!"
                    return result
                case '3':
                    pass
