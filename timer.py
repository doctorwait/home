from time import time


def timer(func):
    """
    Декоратор замеряет время исполнения одной функции (предположительно, применимо к классу)
    :param func: функция или класс (возможно)
    :return: ссылка на изменённую функцию
    """
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        time_res = end - start
        parsing_for_name = func.__repr__().split(' ')
        print(f'Исполнение {parsing_for_name[1]} заняло {time_res} секунд.')
        return res
    return wrapper
