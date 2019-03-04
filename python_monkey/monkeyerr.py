# -*- coding: utf-8 -*-
import re

def remove(errcode, err):
        if errcode == "crash" and re.findall("System appears", err):
            code = 0
        elif errcode == "exception" and re.search('IOException', err):
            code = 0
        elif errcode == "exception" and re.search('Exception from procrank', err):
            code = 0
        else:
            code = 1
        return code

def get_err(address):

    pattern = {"anr": re.compile("ANR"),
               "crash": re.compile("crash"),
               "exception": re.compile("\n(.*Exception.*)\n")}
    with open(address, "r") as f:
        monkey_log = f.read()
    log = [l for l in monkey_log.split("\n") if l != ""]
    a = pattern["exception"].findall(monkey_log, re.M)


    monkey_err = {}
    new_err = {}
    for status, pattern in pattern.items():
            monkey_err[status] = [i for i in log if pattern.findall(i)]
    for errcode in monkey_err:
        new_err[errcode] = [err for err in monkey_err[errcode] if remove(errcode, err) == 1]

    return new_err

def print_err(monkey_err):
    print("错误总结：")
    for errcode in monkey_err:
        print("{}: {} 个".format(errcode, len(monkey_err[errcode])))
    print("\n错误详情：")
    for errcode in monkey_err:
        if len(monkey_err[errcode]) != 0:
            print(errcode + ":")
            for i in monkey_err[errcode]:
                print(i)



if __name__ == '__main__':
    address = r"C:\Users\mhm\Desktop\livemonkey\livemonkey\Monkey_mi4w\result\20181228202132\monkey.log"
    monkey_err = get_err(address)
    print_err(monkey_err)

