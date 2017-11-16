# -*- coding: utf-8 -*-
from input import string_to_evaluate


def are_letters_unique(input_string):
    return len(set(input_string)) == len(input_string)


def run():
    are_letters_unique(string_to_evaluate)


if __name__ == '__main__':
    run()
