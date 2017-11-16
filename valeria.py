# -*- coding: utf-8 -*-
from input import string_to_evaluate


def is_unique(string):
    char_dict = {}
    for char in string:
        if char_dict.get(char):
            return False
        else:
            char_dict[char] = True
    return True


def run():
    is_unique(string_to_evaluate)


if __name__ == '__main__':
    run()
