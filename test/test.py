# 引入模块
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import openpyxl  # openpyxl是处理Excel表格的模块
import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)


class DrawTest(unittest.TestCase):
    def setUp(self):
        # 实例化浏览器
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        sleep(2)

    def tearDown(self):
        self.driver.quit()

    # 定位登录元素
    def get_element(self, by, value):
        # /html[1]/body[1]/div[1]/div[1]/input[1]    sumbit
        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'classname':
            element = self.driver.find_element_by_class_name(value)
        else:
            element = self.driver.find_element_by_xpath(value)
        return element

    # 测试组
    def test_draw(self):
        ex_tag = '/html/body/div[1]/div[1]/div[5]/div/div/div[3]/ul/'
        tag = [ex_tag+'li[1]/a/span[2]', ex_tag +
               'li[2]/a/span[2]', ex_tag + 'li[3]/a/span[2]']
        excellist = []
        for x in tag:
            value1 = self.get_element('xpath', x).text
            excellist.append(value1)
        print(excellist[0])
        excellist.clear()
        print(excellist)


if __name__ == "__main__":
    unittest.main()
    quit()
