# 引入模块
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import openpyxl  # openpyxl是处理Excel表格的模块
import sys
import os
base_path = os.getcwd()+'/抽奖概率/抽奖测试'
sys.path.append(base_path)


class DrawTest(unittest.TestCase):
    def setUp(self):
        # 实例化浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("https://car.velo.com.cn/0818/index.html?bg=1")
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

    def load_excel(self):
        '''
        加载excel
        '''
        open_value = openpyxl.load_workbook(base_path+'/data.xlsx')
        return open_value

    def excel_write_data(self, rows, cols, value):
        '''写入数据，即执行结果回写'''
        wb = self.load_excel()  # 获取表格
        wr = wb.active  # 激活表格，然后可写入
        wr.cell(rows, cols, value)  # 写入数据
        wb.save(base_path+"/data.xlsx")  # 保存数据

    # 测试组
    def test_draw(self):
        ex_tag = '/html/body/div[2]/'
        tag = [ex_tag+'div', ex_tag+'span']
        self.get_element(
            'xpath', '/html/body/div[1]/div/input').send_keys('s123456')
        self.get_element('classname', 'sumbit').click()
        sleep(2)
        i = 0
        all = 10
        while i < all:
            excellist = []
            elestart = self.get_element('classname', 'start')
            elestart.click()
            sleep(3)
            elestop = self.get_element('classname', 'bgStop')
            if (elestop.is_displayed() == True):
                elestop.click()
                sleep(2)
                for x in tag:
                    value1 = self.get_element('xpath', x).text
                    excellist.append(value1)
                self.excel_write_data(i+1, 1, excellist[0])
                self.excel_write_data(i+1, 2, excellist[1])
            else:
                sleep(2)
                elestart.click()
            i = i + 1


if __name__ == "__main__":
    unittest.main()
    quit()
