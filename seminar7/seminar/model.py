def get_phonebook():

    with open('directory.csv', 'r', encoding='utf-8') as file:
        result = []
        for i in file:
            result.append(file.readline().split(','))
    return result 

def add_contact():
    