# -*- coding: utf-8 -*-
from .logger import logger


class GestureAction(object):
    def __init__(self, driver):
        self.driver = driver

    def swipe_on(self, direction):
        """
        手机屏幕的上下左右滑动
        :param direction: 滑动方向：left,right,up,down
        :return: None
        """
        if direction == 'left':
            self._swipe_left(self.driver)
        elif direction == 'right':
            self._swipe_right(self.driver)
        elif direction == 'up':
            self._swipe_up(self.driver)
        elif direction == 'down':
            self._swipe_down(self.driver)
        else:
            logger.infout("<Swipe>: enter wrong direction")
            return None

    def _get_window_size(self, driver):
        """
        获取手机屏幕的尺寸
        :return: width, height
        """
        size = driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def _swipe_left(self, driver):
        width, height = self._get_window_size(driver)
        x1 = width / 10 * 9
        x2 = width / 10 * 2
        y = height / 2
        driver.swipe(x1, y, x2, y)

    def _swipe_right(self, driver):
        width, height = self._get_window_size(driver)
        x1 = width / 10 * 2
        x2 = width / 10 * 9
        y = height / 2
        driver.swipe(x1, y, x2, y)

    def _swipe_down(self, driver):
        width, height = self._get_window_size(driver)
        y1 = width / 10 * 2
        y2 = width / 10 * 9
        x = height / 2
        driver.swipe(x, y1, x, y2)

    def _swipe_up(self, driver):
        width, height = self._get_window_size(driver)
        y1 = width / 10 * 9
        y2 = width / 10 * 2
        x = height / 2
        driver.swipe(x, y1, x, y2)
