# -*- coding: utf-8 -*-
from .baseRes import Element

class BaiduRes(Element):
    def __init__(self, driver):
        super().__init__(driver)

        self.url = 'https://www.baidu.com'

        self.input_box = self.get_element(value='kw')
        self.search_button = self.get_element(value='su')
        self.nav_top = self.get_element(value='u1')
        self.news_link = self.get_element_through_father(self.nav_top, by='name', value='tj_trnews')

