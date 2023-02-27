import os
import datetime
import functools


def logger(old_function):
    @functools.wraps(old_function)
    def new_function(*args, **kwargs):
        dt = datetime.datetime.now()
        value = old_function(*args, **kwargs)
        with open('my_main.log', 'a', encoding='utf-8') as file:
            file.write(
                f'Наименование функции: {old_function.__name__}\n'
                f'Дата и время вызова функции: {dt}\n'
                f'Аргументы функции: {args} и {kwargs}\n'
                f'Возвращаемое значение: {value}\n'
            )
        return value

    return new_function


@logger
def print_people_name(document_num):
    number = input('Введите номер документа: ')
    for element in document_num:
        if element['number'] == number:
            res = element['name']
            return res
    return ('Документа с таким номером не существует')


@logger
def get_shelf_number(shelf_num):
    command = input('Введите номер документа: ')
    for key, value in shelf_num.items():
        if command in value:
            return key
    return 'Документа с таким номером не существует'


@logger
def get_list_of_docs(doc_list):
    for element in doc_list:
        print(element['type'], element['number'], element['name'])


@logger
def add_document(new_documents, new_directories):
    a = input('Укажите тип документа: ')
    b = input('Укажите номер документа: ')
    c = input('Укажите имя владельца документа: ')
    adding_documents = {"type": a, "number": b, "name": c}
    new_documents.append(adding_documents)
    print(new_documents)

    d = input('Укажите номер полки для документа: ')
    # for element in new_directories:
    if d in new_directories.keys():
        new_directories[d].append(adding_documents["number"])
        print(new_directories)
    else:
        return 'Такой полки не существует'


@logger
def delete_document(del_doc, del_dictory):
    doc_numb = input('Введите номер документа:')
    for element in del_doc:
        if doc_numb == element['number']:
            del element['type'], element['number'], element['name']
            return del_doc

    for key, value in del_dictory.items():
        if doc_numb in value:
            value.remove(doc_numb)


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

while True:
    print('Существующие команды: p, s, l, a, d')
    command = input('Выберите команду: ')
    if command == 'p':
        print(f'Имя человека, которому принадлежит введенный документ: {print_people_name(documents)}')

    elif command == 's':
        print(f'Номер полки, на которой лежит запрашиваемый документ:  {get_shelf_number(directories)}')

    elif command == 'l':
        print(f'Список всех документов {get_list_of_docs(documents)}')

    elif command == 'a':
        print(f'Добавлен новый документ: {add_document(documents, directories)}')

    elif command == 'd':
        print(f'Удален документ с введенным номером:  {delete_document(documents, directories)}')
        break
