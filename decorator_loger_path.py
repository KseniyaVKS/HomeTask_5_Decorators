import datetime
import os
from functools import wraps


def logger2(path):
    current_dir = os.getcwd()

    def __logger(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):

            with open(current_dir + '\\' + path, 'a', encoding='utf-8') as log_file:
                start = datetime.datetime.now()
                result = old_function(*args, **kwargs)

                info = f'Дата и время вызова функции {start}\n' \
                       f'Вызвана {old_function.__name__} с аргументами {args} и {kwargs}.\n' \
                       f'Возвращаемое значение {result}\n\n'
                log_file.writelines(info)

                return result

        return new_function

    return __logger
