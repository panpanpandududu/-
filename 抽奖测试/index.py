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
        self.driver.get("http://h5.zwlearn.com/bigScreenDraw/aodi-0116-10man")
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
        # tag = [ex_tag+'div', ex_tag+'span']
        listname = []
        for i in range(1, 10):
            name = 'name0'+str(i)
            listname.append(name)
        listname.append('name10')
        self.get_element(
            'xpath', '/html/body/div[1]/div/input').send_keys('s123456')
        self.get_element('classname', 'sumbit').click()
        sleep(5)
        i = 0
        all = 2
        while i < all:
            elestart = self.get_element(
                'classname', "normal")
            elestart.click()
            sleep(3)
            elestop = self.get_element(
                'xpath', "//div[@class='bgStop stop']")
            if (elestop.is_displayed() == True):
                btn = self.driver.find_elements_by_class_name("normal")[1]
                self.driver.execute_script("arguments[0].click();", btn)
                sleep(3)
            for index, value in enumerate(listname):
                value1 = self.get_element('classname', value).text
                self.excel_write_data(index+1, i+1, value1)
            i = i + 1


if __name__ == "__main__":
    unittest.main()
    quit()
