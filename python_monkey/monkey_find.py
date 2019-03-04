# -*- coding: utf-8 -*-
import os, re


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

def get_err(path):
    pattern = {"anr": re.compile("ANR"),
               "crash": re.compile("crash"),
               "exception": re.compile("Exception")}
    with open(path, 'r', encoding='utf-8') as f:
        monkeylog = f.read()
    monkey_err = {}
    new_err = {}
    for status, pattern in pattern.items():
        log = [l for l in monkeylog.split("\n") if l != ""]
        monkey_err[status] = [i for i in log if pattern.findall(i)]
    for errcode in monkey_err:
        new_err[errcode] = [err for err in monkey_err[errcode] if remove(errcode, err) == 1]

    return new_err


def find_file(address, pkgversion):
    monkeyfile = [file for file in os.listdir(address) if re.match("^Monkey", file) !=None]
    data = {}
    for monkey in monkeyfile:
        monkeypath = os.path.join(address, monkey, "TestResult")
        monkeydir = os.listdir(monkeypath)
        for pkg in monkeydir:
            if pkg == "WaliLive"+pkgversion:
                walipath = os.path.join(monkeypath, pkg)
                data[monkey] = [os.path.join(walipath, i, "monkey.log") for i in os.listdir(walipath)]
    return data


if __name__ == '__main__':
    address = r"C:\Users\mhm\Desktop\monkey"
    pkgversion = "5.2.18"
    monkeydata = find_file(address, pkgversion)
    for name, filepath in monkeydata.items():
        print(name)
        for path in filepath:
            err = get_err(path)
            if len(err['anr']) != 0 or len(err['crash']) != 0 or len(err['exception']) != 0:
                print(err)
            else:
                print("OK!")
