# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from threading import current_thread
from threading import local


class Logger(object):
    """
    自定义的Logger类:
        * 自定义了debug,info,warning,error,critical的格式
        * 提供了缩进格式的支持
        * 可以按照不同的线程组织
        * 提供了Label的绘制
    """

    # 初始化logger的默认配置
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s:%(message)s')

    @classmethod
    def enter(cls, msg=None, *args, **kwargs):
        """
        生成一行DEBUG信息, 用于进入函数或者结构, 与exit()配对使用生成进出函数的日志.
        调用enter()函数会增加日志的缩进层次, 后续的日志都以此行为首行进行悬挂缩进.
        :param msg: 格式化字符串, 常用的格式如'{}.method_name(param1={}, param2={}) - <Class_Name>'
        :param args, kwargs: 用于格式化log的参数, 通常第一个是实例的标示名, 后面是函数的参数
        :例子
        class Foo:
            def foo(self, p1):
                Logger.enter('{}.foo1(p1={}) - <Foo>', self.instance, p1)
                ...
                Logger.exit()
        """
        if msg:
            cls.dbgout(msg, *args, **kwargs)
        cls._increase_deep()

    @classmethod
    def exit(cls, msg=None, *args, **kwargs):
        """
        生成一行DEBUG信息, 用于退出函数或者结构, 与exit()配对使用生成进出函数的日志.
        调用exit()函数会减少后续日志的缩进层次.
        :param msg: 格式化字符串, 常用的格式如'{}.method_name(param1={}, param2={}) - <Class_Name>'
        :param args, kwargs: 用于格式化log的参数, 通常第一个是实例的标示名, 后面是函数的参数
        :例子
        class Foo:
            def foo(self, p1):
                Logger.enter('{}.foo1(p1={}) - <Foo>', self.instance, p1)
                result = ...
                Logger.exit('return {}', result)
        """
        if msg:
            cls.dbgout(msg, *args, **kwargs)
        cls._decrease_deep()

    @classmethod
    def dbgout(cls, msg, *args, **kwargs):
        """
        生成一行DEBUG日志. 如果消息以'Enter: '或者'Exit: '开头,则会影响缩进.
        :param msg: 格式化字符串, 常用的格式如'{}.method_name(param1={}, param2={}) - <Class_Name>'
        :param args, kwargs: 用于格式化log的参数, 通常第一个是实例的标示名, 后面是函数的参数.
        """
        if cls._logger().level > logging.DEBUG:
            return
        cls._output(current_thread().name, logging.debug, msg, *args, **kwargs)

    @classmethod
    def infout(cls, msg, *args, **kwargs):
        """
        生成一行INFO日志. 如果消息以'Enter: '或者'Exit: '开头,则会影响缩进.
        :param msg: 格式化字符串, 常用的格式如'{}.method_name(param1={}, param2={}) - <Class_Name>'
        :param args, kwargs: 用于格式化log的参数, 通常第一个是实例的标示名, 后面是函数的参数.
        """
        if cls._logger().level > logging.INFO:
            return
        cls._output(current_thread().name, logging.info, msg, *args, **kwargs)

    @classmethod
    def wrnout(cls, msg, *args, **kwargs):
        """
        生成一行WARNING日志. 如果消息以'Enter: '或者'Exit: '开头,则会影响缩进.
        :param msg: 格式化字符串, 常用的格式如'{}.method_name(param1={}, param2={}) - <Class_Name>'
        :param args, kwargs: 用于格式化log的参数, 通常第一个是实例的标示名, 后面是函数的参数.
        """
        if cls._logger().level > logging.INFO:
            return
        cls._output(current_thread().name, logging.warning, msg, *args, **kwargs)

    @classmethod
    def errout(cls, msg, *args, **kwargs):
        """
        生成一行ERROR日志. 如果消息以'Enter: '或者'Exit: '开头,则会影响缩进.
        :param msg: 格式化字符串, 常用的格式如'{}.method_name(param1={}, param2={}) - <Class_Name>'
        :param args, kwargs: 用于格式化log的参数, 通常第一个是实例的标示名, 后面是函数的参数.
        """
        if cls._logger().level > logging.INFO:
            return
        cls._output(current_thread().name, logging.error, msg, *args, **kwargs)

    @classmethod
    def criout(cls, msg, *args, **kwargs):
        """
        生成一行CRITICAL日志. 如果消息以'Enter: '或者'Exit: '开头,则会影响缩进.
        :param msg: 格式化字符串, 常用的格式如'{}.method_name(param1={}, param2={}) - <Class_Name>'
        :param args, kwargs: 用于格式化log的参数, 通常第一个是实例的标示名, 后面是函数的参数.
        """
        if cls._logger().level > logging.INFO:
            return
        cls._output(current_thread().name, logging.critical, msg, *args, **kwargs)

    @classmethod
    def label(cls, msg, h_char='-', v_char='+', blank_line=False, enter=False):
        """
        绘制label, 默认格式如下
        ---------------------
        +       TITLE       +
        ---------------------
        :param msg: label的标题
        :param h_char: 定义水平边框所使用的字符, 如指定h_char="="
        :param v_char: 定义垂直边框所使用的字符, 如指定v_char="-*-"
        ======================
        -*-      TITLE     -*-
        ======================
        :param blank_line: 是否有空行, 默认为False, 有空行的效果:
        ---------------------
        +                   +
        +       TITLE       +
        +                   +
        ---------------------
        :param enter:
        """

        # 消息的长度
        len_msg = len(msg)

        # 垂直分割符的长度
        len_v = len(v_char)

        # 水平分隔符只能是一个字节, 取第一个字节
        h_char = h_char[0]

        # 一行的长度: 消息长度的左右加上align
        align = 1
        len_msg = align + len_msg + align

        # 一行的长度: 左\右分别再加上垂直分割符的宽度
        len_line = len_v + len_msg + len_v

        border = "{{:{}^{}}}".format(h_char, len_line).format('')
        label = "{{0}}{{1:^{}}}{{0}}".format(len_msg).format(v_char, msg)
        if blank_line:
            blank = "{{0}}{{1:{}}}{{0}}".format(len_msg).format(v_char, '')
            lines = [border, blank, label, blank, border]
        else:
            lines = [border, label, border]
        for line in lines:
            cls._output(current_thread().name, logging.info, line)
        if enter:
            cls._increase_deep()

    @classmethod
    def set_catch_type(cls, type_='Thread-'):
        """
        设置缓存哪些线程的日志.
        主线程的名字为'MainThread', 其他线程的名字为'Thread-n'
        如果需要缓存所有线程的日志, 可以将type参数设置为空
        :param type_: 指定要缓存哪些线程的日志, 会用此参数和线程名字做startswith()操作
        """
        cls.__catch_type = type_

    @classmethod
    def dump_caught_log(cls, prefix=''):
        """
        在多线程的环境中, 各个线程的日志会混杂在一起, 难以辨别.
        可以缓存下某些线程的日志, 最后按照线程进行分组输出.
        :param prefix: 可以指定输出某些线程的日志, 采用startswith()操作进行过滤
        """
        for thread in cls.__caught_log:
            if not thread.startswith(prefix):
                continue
            for l in cls.__caught_log[thread]:
                level = '{}:{}'.format(l.level.upper(), cls._align(l.level))
                indent = cls._indent(l.deep)
                print('{}-{}[{:<10}]{} {}'.format(l.time, level, thread, indent, l.line))

    # logger对象
    __logger = logging.getLogger()

    @classmethod
    def _logger(cls):
        """
        获取logger对象, 并缓存起来
        :return: 缓存的logger对象
        """
        if cls.__logger:
            return cls.__logger
        cls.__logger = logging.getLogger()
        return cls.__logger

    # 线程局部存储 - 用于存储每个线程的日志的缩进深度
    __thread_data = local()

    @classmethod
    def _get_deep(cls):
        """
        每个线程的日志是独立的, 获取本线程日志缩进的深度
        :return: 整数, 日志缩进的深度
        """
        deep = getattr(cls.__thread_data, 'deep', None)
        if deep:
            return deep
        cls.__thread_data.deep = 0
        return 0

    @classmethod
    def _increase_deep(cls):
        """
        每个线程的日志是独立的, 增加本线程日志缩进的深度
        """
        deep = cls._get_deep()
        cls.__thread_data.deep = deep + 1

    @classmethod
    def _decrease_deep(cls):
        """
        每个线程的日志是独立的, 减少本线程日志缩进的深度
        如果日志深度已经是0, 则什么都不做
        """
        deep = cls._get_deep()
        if deep > 0:
            cls.__thread_data.deep = deep - 1

    # 定义tab stop, 默认2个空格, 用于计算缩紧和对齐
    __tab = '  '

    @classmethod
    def _indent(cls, deep):
        """
        根据缩进深度,返回需要缩进的空格
        :param deep: 缩进深度
        :return: 需要缩进的空格
        """
        return cls.__tab * deep

    @classmethod
    def _align(cls, level):
        """
        logger的输出方法包括:debug, infout, warn, error, critical.
        每行日志,会带有相应的标记: DEBUG, INFO, WARN, ERROR, CRITICAL
        这造成了输出的日志内容不能对齐,因此需要补上一定数量的空格.
        :param level: 输出方法
        :return: 需要补齐的空格
        """
        longest = len('CRITICAL')
        length = len(level)
        return ' ' * (longest - length)

    class LogItem(object):
        """
        LogItem类的每个实例代表一条Log, 包括时间/缩进/内容/Level
        """

        def __init__(self, deep, line, level):
            """
            :param deep: 缩进
            :param line: 内容
            """
            self.time = datetime.now()
            self.deep = deep
            self.line = line
            self.level = level

    # 缓存的日志: 以线程名作为Key, 已_LogItem的数组作为Value
    __caught_log = {}
    # 默认缓存主线程以外的log
    __catch_type = 'Thread-'

    @classmethod
    def _output(cls, thread_name, method, msg, *args, **kwargs):
        """
        按照自定义的格式, 为各个线程产生日志.
        如果消息以'Enter: '开头, 则增加缩进
        如果消息以'Exit: '开头,则减少缩进
        :param thread_name: 线程名
        :type thread_name: str
        :param method: 输出日志的底层函数, 有debug, infout, critical, warn, error
        :type method: function
        :param msg: 消息的格式化字符串
        :type msg: str
        :param args, kwargs: 格式化参数
        """
        output = msg.format(*args, **kwargs)
        if output.startswith('Exit: '):
            cls._decrease_deep()
        if thread_name not in cls.__caught_log:
            cls.__caught_log[thread_name] = []
        deep = cls._get_deep()
        for line in output.splitlines():
            if not line:
                continue
            if thread_name.startswith(cls.__catch_type):
                cls.__caught_log[thread_name].append(cls.LogItem(deep, line, method.__name__))
            prefix = '{}[{:<10}] {}'.format(cls._align(method.__name__), thread_name, cls._indent(deep))
            msg = prefix + line
            method(msg)
        if output.startswith('Enter: '):
            cls._increase_deep()


logger = Logger

if __name__ == '__main__':
    logger.enter("This is an enter msg: {}", 123)
    logger.dbgout("This is a debug msg: {}", 123)
    logger.dbgout("Enter: this is a debug msg with prefix Enter: {}", 123)
    logger.infout("This is a info msg: {}", 123)
    logger.wrnout("Exit: This is a warn msg with prefix Exit: {}", 123)
    logger.errout("This is an error msg: {}", 123)
    logger.criout("This is a critical msg: {}", 123)
    logger.exit("This is an exit msg: {}", 123)

    logger.set_catch_type('')
    logger.label("1")
    logger.set_catch_type('Main')
    logger.label("12345", v_char='*', h_char='=', blank_line=True)
    import time

    time.sleep(1)
    logger.dump_caught_log('Main')
