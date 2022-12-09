import ui
import base
import export
import logger
import import_data


def run():
    logger.logging.info('Запуск программы.')
    running = True

    while running:
        ui.menu()
        user_choice = ''
        while not user_choice:
            user_choice = input('Выбирите действие: ')
            match user_choice:
                case '1':
                    base.show_directory()
                case '2':
                    base.add_contact()
                case '3':
                    base.simple_search()
                case '4':
                    id_ = base.get_id()
                    res_search = base.id_search(id_)
                    if res_search == None:
                        result = 'Сотрудник с таким id не найден!'
                        ui.print_data(result)
                    else:
                        ui.print_data(res_search)
                        result = res_search
                    logger.logging.info(
                        f'Поиск сотрудника с id {id_}. Результат: {result}')
                case '5':
                    id_ = base.get_id()
                    res_search = base.id_search(id_)
                    if res_search == None:
                        result = 'Сотрудник с таким id не найден!'
                        ui.print_data(result)
                    else:
                        print(res_search)
                        if base.confirm('Удалить данные о сотруднике?'):
                            base.delete_worker(id_)
                            result = 'Данные о сотруднике успешно удалены!'
                            ui.print_data(result)
                        else: 
                            result = "Отмена операции!"
                            ui.print_data(result)
                    logger.logging.info(
                        f'Удаление данных о сотруднике с id {id_}. Результат: {result}')
                case '6':
                    result = export.export_file()
                    ui.print_data(result)
                    logger.logging.info(
                        f'Экспорт данных. Результат: {result}.')
                case '7':
                    file_name = base.get_file_name()
                    upload_result = import_data.upload_data(file_name)
                    ui.print_data(upload_result)
                    logger.logging.info(
                        f'Импорт данных из файла {file_name}. {upload_result}')

                case '0':
                    running = False
                    logger.logging.info('Выход из программы.')
