# -*- coding: utf-8 -*-
from enum import Enum

class Name(Enum):
    grade1 = "Bloker"
    grade2 = 'Critical'
    grade3 = 'Major'
    grade4 = 'Minor'

class Color(Enum):
    color1 = 'blue'
    color2 = 'red'
    color3 = 'yellow'
    color4 = 'green'

class Table(Enum):
    sub_table = 'submit_bug_of_this_week'
    rest_table = 'rest_bug_of_this_week'
    old_rest_table = 'rest_bug_of_last_week'

if __name__ == '__main__':
    print(Table['sub_table'].value)

