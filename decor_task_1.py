import json
from datetime import datetime


def dec_task_1(old_function):

    def new_function(*args, **kwargs):

        function_return = old_function(*args, **kwargs)

        log_list = {
            'name': old_function.__name__,
            'datetime': datetime.now(),
            'args': args,
            'kwargs': kwargs,
            'return': function_return
        }

        with open('log.json', 'w', encoding='utf-8') as file_obj:
            json.dump(log_list, file_obj, ensure_ascii=False, indent=4, default=str)

        return function_return

    return new_function
