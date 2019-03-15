# -*- coding: utf-8 -*-
"""
本文主要用于手机APP的安装，使用多线程+adb命令实现

"""
import argparse
import subprocess
import re
import threading


class ArgParser():
    """
    命令行参数类
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-s', '--serial', help='手机serial号，只安装一个手机，默认是安装全部手机')
        self.parser.add_argument('-p', '--path', help='App 路径')
        self.parser.add_argument('-g', '--pkg', help='包名', nargs='?', default='com.wali.live')

        self.args = self.parser.parse_args()

class MyTread(threading.Thread):
    """
    自定义线程类
    """
    def __init__(self, name, pkg, path):
        super(MyTread, self).__init__()
        self.name = name
        self.pkg = pkg
        self.path = path
    def run(self):
        print("安装线程已经启动", self.name)
        print("run in task", self.name, threading.current_thread(), threading.active_count())
        APPinstall().install_one(self.name, self.pkg, self.path)

class APPinstall():
    """
    软件安装
    """
    def __init__(self):
        self.serial = ''
        self.path = ''
        self.pkg = ''
        self.pre_cmd = 'adb '

    def install_all(self):
        """
        安装全部的手机，默认选项
        :return:
        """
        devices_result = self.get_popen('adb devices')
        serials = re.findall('\r\n(.*?)\tdevice', devices_result)
        threads = []
        for serial in serials:
            t = MyTread(serial, self.pkg, self.path)
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def install_one(self, serial='', pkg='', path=''):
        """
        一部手机的安装，如果serial号不为空的话
        :param serial:
        :param pkg:
        :param path:
        :return:
        """
        code = self.pre_install(serial, pkg)
        if not code:
            install_cmd = self.pre_cmd + 'install %s' % path
            install_result = self.get_popen(install_cmd)
            if re.search('Success', install_result):
                return 0
            else:
                return 1
        else:
            return 1

    def pre_install(self, serial='', pkg=''):
        """
        安装预准备操作
        :param serial:
        :param pkg:
        :return:
        """
        self.pre_cmd = 'adb -s %s ' % serial if serial else self.pre_cmd
        ensure_cmd = self.pre_cmd + 'shell pm list package'
        ensure_result = self.get_popen(ensure_cmd)
        if re.search(pkg, ensure_result):
            uninstall_cmd = self.pre_cmd + "uninstall %s" % pkg
            uninstall_result = self.get_popen(uninstall_cmd)
            if re.search('Success', uninstall_result):
                return 0
            else:
                return 1
        else:
            return 0
    def get_popen(self, cmd):
        """
        获取adb 运行的结果
        :param cmd:
        :return:
        """
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        data = result.communicate()[0].decode()
        return data

    def go(self):
        args = ArgParser().args
        print(args)

        self.serial = args.serial
        self.path = args.path
        self.pkg = args.pkg

        if self.serial:
            self.install_one(self.serial, self.pkg, self.path)
        else:
            self.install_all()

if __name__ == '__main__':
    APPinstall().go()