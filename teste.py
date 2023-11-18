# -*- coding: utf-8 -*-
import random

def rd_string(length):
    """
    Criando Strings aleatórias usando casting
    """
    str_rd = ""
    while(len(str_rd)<=length):
        str_rd += '%c' % random.randint(97, 122)
    return str_rd


# Testing
for n in range(0, 1):
    print(rd_string)
