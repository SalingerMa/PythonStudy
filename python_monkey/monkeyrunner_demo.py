# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# connect to device
device = MonkeyRunner.waitForConnection(3,"fdsd48786")

# start app
device.startActivity('com.wali.live/.main.LiveMainActivity')
MonkeyRunner.sleep(3)

# click search box
device.touch(485, 128, "DOWN_AND_UP")
MonkeyRunner.sleep(1)

# send keys
device.type("test")
MonkeyRunner.sleep(1)

# press enter btn
device.press('KEYCODE_ENTER', "DOWN_AND_UP")
MonkeyRunner.sleep(1)

# click search btn
device.touch(1014, 134, "DOWN_AND_UP")
MonkeyRunner.sleep(2)

# 
image = device.takeSnapshot()
image.writeToFile(r'C:\python_monkey\shot1.png','png')

# press back btn
device.press('KEYCODE_BACK', "DOWN_AND_UP")
MonkeyRunner.sleep(1)