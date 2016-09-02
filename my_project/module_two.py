# -*- coding: utf-8 -*-

from my_project import module_one


def custom_count(data, count):
    """
    :param data: str
    :param count: int
    :return: list
    """
    c = module_one.get_char_count(data)
    return [(i, j) for i, j in c.items() if j >= count]
