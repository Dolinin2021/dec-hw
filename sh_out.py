from decor_task_2 import dec_task_2


@dec_task_2('D:\\')
def shelf_output(dict_name, number=None):
    number = input('Введите номер документа: ')
    for key, value in dict_name.items():
        if number in value:
            print(f"Номер полки, на которой лежит этот документ: {key}")
            break
    else:
        print('Неправильный ввод данных. Попробуйте еще раз.')