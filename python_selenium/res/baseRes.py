# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Element(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by='id', value=None):
        ele_type = self._get_element_type(by)

        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((ele_type, value))
        )

    def get_elements(self, by='id', value=None):
        ele_type = self._get_element_type(by)

        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((ele_type, value))
        )

    def get_element_through_father(self, father, by='id', value=None):
        ele_type = self._get_element_type(by)

        return father.find_element(ele_type, value)


    def _get_element_type(self, type_):
        if type_ is not None:
            if type_ == 'id':
                type_ = By.ID
            elif type_ == 'class':
                type_ = By.CLASS_NAME
            elif type_ == 'css':
                type_ = By.CSS_SELECTOR
            elif type_ == 'link_text':
                type_ = By.LINK_TEXT
            elif type_ == 'part_link_text':
                type_ = By.PARTIAL_LINK_TEXT
            elif type_ == 'name':
                type_ = By.NAME

        return type_