import configparser
conf = configparser.ConfigParser()
conf.read(r'C:\Users\mhm\Desktop\study\config.ini')
emailName = conf.get('flask', 'name')
emailPasswd = conf.get('flask', 'passwd')