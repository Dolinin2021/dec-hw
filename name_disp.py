from decor_task_1 import dec_task_1


@dec_task_1
def name_display(list_name, number=None):
    number = input('Введите номер документа: ')
    for output in list_name:
        if output['number'] == number:
            print(f"Имя человека, которому этот документ принадлежит: {output['name']}")
            break
    else:
        print('Неправильный ввод данных. Попробуйте еще раз.')