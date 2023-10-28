"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

"""


def swap_key_value(**kwargs):
    """
    Swaps keys and values
    :param kwargs: any number of key elements
    :return: dictionary
    """
    result = {}
    for key, value in kwargs.items():
        str_value = str(value)
        if result.setdefault(str_value, [key]) != [key]:
            result[str_value].append(key)
        else:
            result.setdefault(str_value, key)
    return result


print(swap_key_value(a=True, b=False, g=False, e=6))

