import sys

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name(number, documents):
    # number = input("Введите номер документа:")
    for doc in documents:
        if doc['number'] == number:
            return (doc['name'])
    else:
        res = "Документа с таким номером не существует."
        return res


def get_shelf(number, directories):
    # number = input("Введите номер документа:")
    for key, value in directories.items():
        for doc in value:
            if number == doc:
                return key
    else:
        return ("Документа с таким номером не существует.")


def get_doc_info(documents):
    docs_list = []
    for doc in documents:
        doc_info = " ".join(list(doc.values()))
        docs_list.append(doc_info)
    docs_string = "\n".join(docs_list)
    return docs_string


def add_doc(shelf_doc, type_doc, number_doc, name, documents, directories):
    # shelf_doc = input("\nВведите номер полки для документа: ")
    # type_doc = input("\nВведите тип документа: ")
    # number_doc = input("\nВведите номер документа: ")
    # name = input("\nВведите имя владельца: ")
    some_dict = {'type': type_doc, 'number': number_doc, 'name': name}
    for key in directories.keys():
        if key == shelf_doc:
            directories[key].append(number_doc)
    if shelf_doc in directories.keys():
        documents.append(some_dict)
        return (f'Документ добавлен в полку {shelf_doc}.', str(some_dict))
    else:
        return ("Такой полки не существует.")


def del_doc(number, documents, directories):
    # number = input('Введите номер документа подлежащего удалению: ')
    for key, value in directories.items():
        for i in value:
            if i == number:
                directories[key].remove(number)
                return (f'Документ номер {number} удален с полки {key}.')

    for doc in documents:
        if doc['number'] == number:
            documents.remove(doc)
            # print(documents)
            # print(directories)
    else:
        return ('Документ с указанным Вами номером не существует.')


def move_doc(shelf, number, directories):
    # shelf = input('Введите номер полки, на которую Вы хотите переместить документ: ')
    # number = input('Введите номер документа, который необходимо переместить: ')
    if shelf in directories:
        for key, value in directories.items():
            if number in value:
                directories[key].remove(number)
                directories[shelf].append(number)
                print(f'Документ {number} перемещен на полку {shelf}.')
                print(directories)
            else:
                print('Указанный Вами документ отсутствует.')
                break
    else:
        print('Указанная Вами полка отсутствует.')


def add_shelf(shelf, directories):
    # shelf = input('Введите номер полки, которую хотите добавить: ')
    if shelf in directories:
        print('Такая полка уже существует.')
        # return res
    else:
        directories[shelf] = []
        print(f'Полка номер {shelf} добавлена.')
        # return res


def error():
    res = 'Введенная Вами команда не существует.'
    return res


text = '''Для работы с документами Вам доступны следующие команды:
	p - найти человека по номеру документа\n
	s – вывести номер полки по номеру документа\n
	l– список документов\n
	a – добавление нового документа\n
	d – удаление документа\n
	m – перемещение документа на другую полку\n
	as - создание полки\n
	q - выход\n
	h - повторно выведет данное меню '''

comm_dict = {
    'p': get_name,
    's': get_shelf,
    'l': get_doc_info,
    'a': add_doc,
    'd': del_doc,
    'm': move_doc,
    'as': add_shelf,
    'q': sys.exit,
    'h': lambda: print(text)
}

# print(text)
# while True:
#     command = input('Введите команду: ')
#     command = command.lower().strip()
#     comm_dict.get(command, error)()
