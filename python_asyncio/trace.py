# -*- coding: utf-8 -*-
class wrapper(object):
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print(f'Trace: {item}')
        return getattr(self.wrapped, item)

if __name__ == '__main__':
    a = [1,2,3]
    x = wrapper(a)
    x.append(4)
    print(x.wrapped)
