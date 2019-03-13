# -*- coding: utf-8 -*-
import argparse
import subprocess
import re
import configparser
import win32api, win32con
import threading
class IniFile():

    def get_desktop(self):
        key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                                  r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', 0,
                                  win32con.KEY_READ)
        return win32api.RegQueryValueEx(key, 'Desktop')[0]

    def __init__(self):
        ini_path = r"%s\WorkNote\test\config.ini" % self.get_desktop()
        self.conf = configparser.ConfigParser()
        self.conf.read(ini_path)

    def read_value(self, section):
        data = self.conf.items(section)
        return {l[0]: l[1] for l in data}

    @classmethod
    def read_inifile(cls):
        pass

class ArgParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-s', '--serial', help='手机serial号，只安装一个手机，默认是安装全部手机')
        self.parser.add_argument('-p', '--path', help='App 路径')
        self.parser.add_argument('-g', '--pkg', help='包名')
        self.parser.add_argument('-f', '--file', help='在文件中搜索参数', action='store_true')

        self.args = self.parser.parse_args()

class MyTread(threading.Thread):

    def __init__(self, name, pkg, path):
        super(MyTread, self).__init__()
        self.name = name
        self.pkg = pkg
        self.path = path
    def run(self):
        # print("安装线程已经启动", self.name)
        # print("run in task", self.name, threading.current_thread(), threading.active_count())
        APPinstall().install_one(self.name, self.pkg, self.path)

class APPinstall():

    def __init__(self):
        self.serial = ''
        self.path = ''
        self.pkg = ''
        self.pre_cmd = ''

    def install_all(self):
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
        # for serial in serials:
        #         code = self.install_one(serial)

    def install_one(self, serial='', pkg='', path=''):
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
        self.pre_cmd = 'adb -s %s ' % serial if serial else 'adb '
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
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        data = result.communicate()[0].decode()
        return data


    def go(self):
        args = ArgParser().args
        data = IniFile().read_value('liveinstall')
        if args.file:
            self.serial = data['serial']
            self.path = data['path']
            self.pkg = data['pkg']
        else:
            self.serial = args.serial if args.serial else data['serial']
            self.path = args.path if args.path else data['path']
            self.pkg = args.pkg if args.pkg else data['pkg']

        if self.serial:
            self.install_one(self.serial, self.pkg, self.path)
        else:
            self.install_all()

if __name__ == '__main__':
    APPinstall().go()
