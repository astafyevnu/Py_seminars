import ui
import base
import export
import logger


#   1 - посмотреть справочник
#     2 - добавить контакт
#     3 - простой поиск по справочнику
#     5 - найти по id
#     5 - найти и удалить контакт(ы)
#     6 - сохранить справочник как...
#     0 - выход''')

def run():
    logger.make_log('Вход в систему')
    running = True
    
    while running:
        ui.menu()
        user_choice = ''
        while not user_choice:
            user_choice = input('Выбирите действие: ')
            match user_choice:
                case '1':
                    base.show_directory()
                    logger.make_log('Вызов справочника')
                case '2':
                    base.add_contact()
                    logger.make_log('Добавление нового контакта')
                case '3':
                    base.simple_search()
                    logger.make_log('Простой поиск по справочнику')
                case '4':
                    pass
                    # base.id_search()
                    # logger.make_log('Поиск контакта по id')
                case '5':
                    pass
            
                case '6':
                    export.export_file()
               
                case '0':
                    running = False
                    logger.make_log('Выход из программы')

def enter_id() -> str:
    contact_id = ''
    while not contact_id:
        contact_id = input('Введите id контакта, который нужно удалить: ')
        while not all(ch.isdigit() for ch in contact_id):
            contact_id = input('id должен быть положительным целым числом: ')
    return contact_id