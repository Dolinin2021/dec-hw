from name_disp import name_display
from sh_out import shelf_output
from pprint import pprint


if __name__ == '__main__':

    instructions = """
    Список команд и их назначение:
    /help - напечатать справку по программе,
    /documents - каталог документов,
    /directories - перечень полок, на которых находятся документы,
    /people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит\n(реализуется функцией name_display),
    /shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится\n(реализуется функцией shelf_output),
    /exit - выход из программы.
    """

    help = """
    Список переменных и их назначение:
    documents - каталог документов,
    directories – перечень полок, на которых находятся документы,
    instructions – список команд и их назначение,
    help – справка по программе,
    list_name – переменная, которая содержит каталог документов, с которым работаем (documents),
    dict_name – переменная, которая содержит перечень полок, на которых находятся документы (directories),
    number – номер документа,
    type_name - тип документа,
    name - имя человека, которому этот документ принадлежит,
    shelf_number - номер полки,
    target_shelf - номер целевой полки.
    """

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


    def main(list_name, dict_name):
        print('Вас приветствует программа по работе с документами компании Python Software.\nПрочитайте инструкцию перед тем, как продолжить.')
        print(instructions)
        while True:
            print()
            user_input = input('Введите команду: ')
            print()
            if user_input == '/help':
                print(help)
            elif user_input == '/documents':
                pprint(documents)
            elif user_input == '/directories':
                print(directories)
            elif user_input == '/people':
                name_display(list_name)
            elif user_input == '/shelf':
                shelf_output(dict_name)
            elif user_input == '/exit':
                break

    main(documents, directories)