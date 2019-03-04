# -*- coding: utf-8 -*-
# coding:utf-8
import os
import sys

device_id = sys.argv[1]

key = os.popen("adb devices -l").read()

for line in os.popen("adb -s " + device_id + " shell ps").read().splitlines():
    if line.find("com.android.commands.monkey") >= 0:
        os.popen("adb -s " + device_id + " shell kill " + line.split()[1])