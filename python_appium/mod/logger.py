# -*- coding:utf-8 -*-
import logging
import datetime
import time
from threading import local
from threading import current_thread

class Logger(object):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s:%(message)s')

    _local = local()
    _thread_log = {}
    # TODO: _group_thread - Time Issue
    _group_thread = True

    @staticmethod
    def get_deep():
        deep = getattr(Logger._local, 'deep', None)
        if deep is None:
            Logger._local.deep = 0
            return 0
        return deep

    @staticmethod
    def increase_deep():
        deep = Logger.get_deep()
        Logger._local.deep = deep + 1

    @staticmethod
    def decrease_deep():
        deep = Logger.get_deep()
        if deep > 0:
            Logger._local.deep = deep - 1

    _tab = '  '

    _align = {
        logging.critical: 0,
        logging.debug: 3,
        logging.info: 4,
        logging.error: 3,
        logging.warn: 1
    }

    @staticmethod
    def enter(msg=None, *args, **kwargs):
        if msg:
            Logger.infout(msg, *args, **kwargs)
        Logger.increase_deep()

    @staticmethod
    def exit(msg=None, *args, **kwargs):
        if msg:
            Logger.infout(msg, *args, **kwargs)
        Logger.decrease_deep()

    @staticmethod
    def dbgout(msg, *args, **kwargs):
        if logging.getLogger().level > logging.DEBUG:
            return
        logger._msg_out(current_thread().name, logging.debug, msg, *args, **kwargs)

    @staticmethod
    def infout(msg, *args, **kwargs):
        if logging.getLogger().level > logging.INFO:
            return
        logger._msg_out(current_thread().name, logging.info, msg, *args, **kwargs)

    @staticmethod
    def errout(msg, *args, **kwargs):
        if logging.getLogger().level > logging.ERROR:
            return
        logger._msg_out(current_thread().name, logging.error, msg, *args, **kwargs)

    @staticmethod
    def wrnout(msg, *args, **kwargs):
        if logging.getLogger().level > logging.WARNING:
            return
        logger._msg_out(current_thread().name, logging.warn, msg, *args, **kwargs)

    @staticmethod
    def criout(msg, *args, **kwargs):
        if logging.getLogger().level > logging.CRITICAL:
            return
        logger._msg_out(current_thread().name, logging.critical, msg, *args, **kwargs)

    @staticmethod
    def _msg_out(thread_name, method, msg, *args, **kwargs):
        output = msg.format(*args, **kwargs)
        if msg.startswith('Exit: '):
            logger.decrease_deep()
        if Logger._group_thread:
            if thread_name.startswith('Thread-'):
                if thread_name not in Logger._thread_log:
                    Logger._thread_log[thread_name] = []
                for line in output.splitlines():
                    Logger._thread_log[thread_name].append(
                        logger._indent() + str(datetime.datetime.now()) + "\t" + line)
                output = ''
        if output:
            align = ' ' * logger._align[method]
            for line in output.splitlines():
                if line:
                    msg = "{}[{:<10}] {}{}".format(align, thread_name, logger._indent(), line)
                    method(msg)
        if msg.startswith('Enter:'):
            logger.increase_deep()

    @staticmethod
    def label(msg, ch_horizon="-", ch_vertical="+", has_blank=False):
        ch_horizon = ch_horizon[0]
        len_v_ch = len(ch_vertical)
        len_h_ch = len(ch_horizon)
        len_msg = len(msg)
        len_line = len_msg + 8 * len_h_ch
        len_total = len_line + 2 * len_v_ch
        border = "{{:{}^{}}}".format(ch_horizon, len_total).format('')
        label = "{{0}}{{1:^{}}}{{0}}".format(len_line).format(ch_vertical, msg)
        if has_blank:
            blank = "{{0}}{{1:{}}}{{0}}".format(len_line).format(ch_vertical, '')
            lines = [border, blank, label, blank, border]
        else:
            lines = [border, label, border]
        for line in lines:
            logger._msg_out(current_thread().name, logging.info, line)

    @staticmethod
    def _indent():
        return logger._tab * logger.get_deep()

    @staticmethod
    def dump_thread_log():

        for thread in sorted(Logger._thread_log):

            len_thread = len(thread)
            len_line = len_thread + 8
            len_total = len_line + 2
            border = "{{:{}^{}}}".format('=', len_total).format('')
            label = "{{0}}{{1:^{}}}{{0}}".format(len_line).format('#', thread)
            blank = "{{0}}{{1:{}}}{{0}}".format(len_line).format('#', '')
            lines = [border, blank, label, blank, border]
            for line in lines:
                logging.debug("{}[{:10}] {}".format(' ' * 3, thread, line))

            for line in Logger._thread_log[thread]:
                logging.debug("{}[{:10}] {}".format(' ' * 3, thread, line))
        Logger._thread_log.clear()

logger = Logger


def sleep(seconds):
    logger.dbgout("sleep({0})", seconds)
    time.sleep(seconds)


