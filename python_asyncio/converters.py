# -*- coding: utf-8 -*-
from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class Htmlize(object):
    def write(self, line):
        print(f'<pre>{line.rstrip()}<pre>')

if __name__ == '__main__':
    import sys
    obj = Uppercase(open('t1.py'), Htmlize())
    obj.process()

