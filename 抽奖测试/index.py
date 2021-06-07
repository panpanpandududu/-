# 引入模块
from handle_excel import excel_data
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
        self.driver = webdriver.Chrome()
        self.driver.get("https://car.velo.com.cn/geely/")
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
        ex_tag = '/html[1]/body[1]/div[3]/div'
        tag = [ex_tag+'[1]', ex_tag+'[2]', ex_tag+'[3]', ex_tag+'[4]', ex_tag+'[5]',
               ex_tag+'[6]', ex_tag+'[7]', ex_tag+'[8]', ex_tag+'[9]', ex_tag+'[10]']
        self.get_element(
            'xpath', '/html[1]/body[1]/div[1]/div[1]/input[1]').send_keys('s123456')
        self.get_element('classname', 'sumbit').click()
        sleep(2)
        i = 0
        all = 10
        while i < all:
            elestart = self.get_element('classname', 'start')
            elestart.click()
            sleep(2)
            elestop = self.get_element('classname', 'stop')
            if (elestop.is_displayed() == True):
                elestop.click()
                for x in tag:
                    value = self.get_element('xpath', x).text
                    excel_data.excel_write_data(tag.index(x)+2, i, value)
            else:
                sleep(2)
                elestart.click()
            i = i + 1


if __name__ == "__main__":
    unittest.main()
    quit()
