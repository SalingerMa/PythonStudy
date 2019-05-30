# -*- coding: utf-8 -*-

import sys
import threading
import time
import unittest
import warnings
from enum import Enum
from queue import Queue
from unittest.signals import registerResult

from unittest.suite import _ErrorHolder

from common.logger import logger

'''
TODO: Class和Module的SetUp(), TearDown()需要处理STDIO
TODO: Class和Module的SetUp(), TearDown()需要处理result
TODO: skip等attribute的处理
'''


class ThreadingTestRunner(unittest.TextTestRunner):
    """
    支持多线程的TestRunner
    """

    attr_name_of_wait_retry = '__need_wait_retry'
    should_stop = False

    class EnumItemType(Enum):
        Module = 1
        Class = 2
        Case = 3

    class EnumItemStatus(Enum):
        Failed = -1
        NotSetUp = 0
        SetUp = 1
        Tested = 2
        TearDown = 3

    class TestTableItem(object):
        def __init__(self, instance, parent, type_):
            self.instance = instance
            self.parent = parent
            self.children = []
            self.item_type = type_
            self.task_count = 0
            self.status = ThreadingTestRunner.EnumItemStatus.NotSetUp

    def __init__(
            self,
            stream=None,
            descriptions=True,
            verbosity=1,
            failfast=False,
            buffer=False,
            resultclass=unittest.TestResult,
            _warnings=None,
            tb_locals=False,
            thread_count=0):

        super(ThreadingTestRunner, self).__init__(
            stream=stream,
            descriptions=descriptions,
            verbosity=verbosity,
            failfast=failfast,
            buffer=buffer,
            resultclass=resultclass,
            warnings=_warnings,
            tb_locals=tb_locals)

        self.mutex = None
        self.result = None
        self.thread_count = 0
        if thread_count > 0:
            self.thread_count = thread_count

    def _gen_test_table(self, test):

        # 生成一个表, 用于保存各个Module, Class, Case的运行状态
        # !!!用Queue()保证线程安全!!!
        self._task_queue = Queue()

        previous_module = None
        previous_class = None
        parent_module = None
        parent_class = None

        # 深度遍历所有的TestCase
        for case in self._enumerate_test_case(test):
            current_class = case.__class__
            current_module = current_class.__module__

            # 开始处理一个新的Module:
            if previous_module != current_module:
                item = ThreadingTestRunner.TestTableItem(
                    sys.modules[current_module],
                    parent_module,
                    ThreadingTestRunner.EnumItemType.Module)
                if parent_module:
                    parent_module.children.append(item)
                self._task_queue.put(item)
                parent_module = item

            # 开始处理一个新的Class:
            if previous_class != current_class:
                item = ThreadingTestRunner.TestTableItem(
                    current_class,
                    parent_module,
                    ThreadingTestRunner.EnumItemType.Class)
                if parent_module:
                    parent_module.children.append(item)
                self._task_queue.put(item)
                parent_class = item

            # 开始处理当前的Case:
            item = ThreadingTestRunner.TestTableItem(
                case,
                parent_class,
                ThreadingTestRunner.EnumItemType.Case)
            self._task_queue.put(item)

            if parent_class:
                parent_class.children.append(item)

            previous_class = current_class
            previous_module = current_module

    def _gen_result(self, register=False):
        result = self._makeResult()
        if register:
            registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        result.tb_locals = self.tb_locals
        return result

    @staticmethod
    def _merge_result(summary, detail):
        summary.testsRun += detail.testsRun
        summary.failures += detail.failures
        summary.expectedFailures += detail.expectedFailures
        summary.unexpectedSuccesses += detail.unexpectedSuccesses
        summary.errors += detail.errors
        summary.skipped += detail.skipped
        summary.shouldStop = detail.shouldStop

    def _run_case(self, queue):
        while True:

            # 从Queue中获取一个item, 如果item的父节点还没有初始化, 则将item放入队尾继续等待
            with queue.not_empty:
                while not len(queue.queue):
                    queue.not_empty.wait()
                item = queue.queue.popleft()
                if item.parent and item.parent.status == ThreadingTestRunner.EnumItemStatus.NotSetUp:
                    queue.queue.append(item)
                    continue
                else:
                    queue.not_full.notify()

            # 父节点初始化失败
            parent = item.parent
            if parent and parent.status == ThreadingTestRunner.EnumItemStatus.Failed:
                self.result.addSkip(item.instance, 'PARENT SETUP FAILED')
                item.status = ThreadingTestRunner.EnumItemStatus.Failed
                logger.errout("PARENT SETUP FAILED, SKIP: {}()", item.instance)

            # 运行TestCase
            elif item.item_type == ThreadingTestRunner.EnumItemType.Case:
                result = self._gen_result()
                if not ThreadingTestRunner.should_stop:
                    item.instance.run(result)
                    ThreadingTestRunner.should_stop = result.shouldStop

                # 如果一个case跑的一半, 需要等某个条件, 框架可以把它放回执行队列中
                wait_retry = getattr(item.instance, ThreadingTestRunner.attr_name_of_wait_retry, 0)

                if wait_retry:
                    queue.task_done()
                    queue.put(item)
                    continue

                with self.mutex:
                    self._merge_result(self.result, result)

                # 是否同一个容器中所有的Item都测试完了
                parent = item.parent
                with self.mutex:
                    parent.task_count -= 1
                    count = parent.task_count
                if not count:
                    parent.status = ThreadingTestRunner.EnumItemStatus.Tested
                    queue.put(parent)

            # 节点需要初始化
            elif item.status == ThreadingTestRunner.EnumItemStatus.NotSetUp:
                setup = None
                if item.item_type == ThreadingTestRunner.EnumItemType.Module:
                    error_name = 'setUpModule (%s)' % item.instance.__name__
                    setup = getattr(item.instance, 'setUpModule', None)
                elif item.item_type == ThreadingTestRunner.EnumItemType.Class:
                    error_name = 'setUpClass (%s)' % item.instance.__name__
                    setup = getattr(item.instance, 'setUpClass', None)
                # noinspection PyBroadException
                try:
                    if setup:
                        setup()
                    item.task_count = len(item.children)
                    item.status = ThreadingTestRunner.EnumItemStatus.SetUp
                except Exception as e:
                    error = _ErrorHolder(error_name)
                    self.result.addError(error, sys.exc_info())
                    logger.errout("FAILED - {}.{}(): {}", item.instance.__name__, setup.__name__, e)
                    item.status = ThreadingTestRunner.EnumItemStatus.Failed

            # 该节点下所有TestCase都跑完了
            elif item.status == ThreadingTestRunner.EnumItemStatus.Tested:
                tear_down = None
                if item.item_type == ThreadingTestRunner.EnumItemType.Module:
                    error_name = 'tearDownModule (%s)' % item.instance.__name__
                    tear_down = getattr(item.instance, 'tearDownModule', None)
                elif item.item_type == ThreadingTestRunner.EnumItemType.Class:
                    error_name = 'tearDownClass (%s)' % item.instance.__name__
                    tear_down = getattr(item.instance, 'tearDownClass', None)
                # noinspection PyBroadException
                try:
                    if tear_down:
                        tear_down()
                    item.status = ThreadingTestRunner.EnumItemStatus.TearDown
                except Exception as e:
                    error = _ErrorHolder(error_name)
                    self.result.addError(error, sys.exc_info())
                    logger.errout("FAILED - {}.{}(): {}", item.instance.__name__, tear_down.__name__, e)
                    item.status = ThreadingTestRunner.EnumItemStatus.Failed

                # 是否同一个容器中所有的Item都测试完毕
                if item.parent:
                    with self.mutex:
                        item.parent.task_count -= 1
                        count = item.parent.task_count
                    if not count:
                        parent.status = ThreadingTestRunner.EnumItemStatus.Tested
                        queue.put(parent)

            queue.task_done()

    def run(self, test):
        self._gen_test_table(test)
        self.result = self._gen_result(True)

        with warnings.catch_warnings():
            if self.warnings:
                # if self.warnings is set, use it to filter all the warnings
                warnings.simplefilter(self.warnings)
                # if the filter is 'default' or 'always', special-case the
                # warnings from the deprecated unittest methods to show them
                # no more than once per module, because they can be fairly
                # noisy.  The -Wd and -Wa flags can be used to bypass this
                # only when self.warnings is None.
                if self.warnings in ['default', 'always']:
                    warnings.filterwarnings('module',
                                            category=DeprecationWarning,
                                            message='Please use assert\w+ instead.')
            start_time = time.time()
            start_test_run = getattr(self.result, 'startTestRun', None)
            if start_test_run is not None:
                start_test_run()
            try:
                if self.thread_count > 0:
                    self.mutex = threading.Lock()
                    self.result._testRunEntered = True
                    workers = []
                    for i in range(self.thread_count):
                        t = threading.Thread(target=self._run_case, args=(self._task_queue,))
                        workers.append(t)
                    for w in workers:
                        w.setDaemon(True)
                        w.start()
                    self._task_queue.join()
                    self.result._testRunEntered = False
                else:
                    test(self.result)
            finally:
                stop_test_run = getattr(self.result, 'stopTestRun', None)
                if stop_test_run is not None:
                    stop_test_run()
            stop_time = time.time()

        time_taken = stop_time - start_time

        self.result.printErrors()
        if hasattr(self.result, 'separator2'):
            self.stream.writeln(self.result.separator2)
        run = self.result.testsRun
        self.stream.writeln("Ran %d test%s in %.3fs" %
                            (run, run != 1 and "s" or "", time_taken))
        self.stream.writeln()

        expected_fails = unexpected_successes = skipped = 0
        try:
            results = map(len, (self.result.expectedFailures,
                                self.result.unexpectedSuccesses,
                                self.result.skipped))
        except AttributeError:
            pass
        else:
            expected_fails, unexpected_successes, skipped = results

        info_list = []
        if not self.result.wasSuccessful():
            self.stream.write("FAILED")
            failed, error = len(self.result.failures), len(self.result.errors)
            if failed:
                info_list.append("failures=%d" % failed)
            if error:
                info_list.append("errors=%d" % error)
        else:
            self.stream.write("OK")
        if skipped:
            info_list.append("skipped=%d" % skipped)
        if expected_fails:
            info_list.append("expected failures=%d" % expected_fails)
        if unexpected_successes:
            info_list.append("unexpected successes=%d" % unexpected_successes)
        if info_list:
            self.stream.writeln(" (%s)" % (", ".join(info_list),))
        else:
            self.stream.write("\n")
        return self.result

    def _enumerate_test_case(self, test):
        """
        TestSuite可以包含子TestSuite, 达到按照树状结构组织TestCase的管理方式.
        此函数作为一个iterable来遍历TestSuite中的每一个TestCase, 深度优先(unittest框架的默认遍历方式).
        :param test: 需要遍历的TestSuite
        :return: 当前迭代的iterator
        """
        for child in test:
            # noinspection PyProtectedMember
            if unittest.suite._isnotsuite(child):
                yield child
            else:
                for item in self._enumerate_test_case(child):
                    yield item
