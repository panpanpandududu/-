
# from handle_excel import excel_data
import ddt
import unittest
import os
import sys
import json
import requests
from unittestreport import TestRunner, HTMLTestRunnerNew
# 解决fiddler抓包出现InsecureRequestWarning警告
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
base_path = os.getcwd()+'/抽奖概率/沃尔沃小程序抽奖概率'
sys.path.append(base_path)

# Excel数据
# datas = excel_data.get_excel_data()


# @ddt.ddt
class MyTestCase(unittest.TestCase):
    def send_post(self, url, data, header):
        # 发送一个post请求
        # 在request.get()\requet.post()里面加参数：verify=False；目的是：移除SSL认证；此时，fiddler就可以抓取到python-requets 请求的包了
        response = requests.post(
            url=url, data=json.dumps(data), headers=header, verify=False)
        res = response.json()
        # 返回res出去
        return res

    # @ddt.data(*datas)
    # 因为就一个参数不用@ddt.unpack
    # def test01(self):
    #     # Headers配置
    #     header = {
    #         'Content-Type': 'application/json',
    #         'openId': "AAEm9hESANdAsZG-4d0TPDAl"
    #     }
    #     addressurl = 'http://8.142.17.120:8080/volvo/taobao/app/20210501/api/tb/address/add'
    #     data = {
    #         "address": "逸仙路逸景佳苑24栋1201",
    #         "city": "上海市",
    #         "county": "上海市",
    #         "name": "潘潘",
    #         "phone": "18155674170",
    #         "province": "上海",
    #         "town": "宝山区"
    #     }
    #     data_json = json.dumps(data)
    #     res = self.send_post(addressurl, data_json, header)
    #     status = res['data']['success']
    #     self.assertTrue(status, msg='状态值不一致')

    @classmethod
    def setUpClass(cls):
        MyTestCase.tinydict = {'1': 0, '2': 0, '3': 0, '4': 0,
                               '5': 0, '6': 0, '7': 0, '8': 0}
        MyTestCase.count = 0

    # @ddt.data(*datas)
    # @ddt.unpack
    def test02(self):
        drawurl = 'http://192.168.3.36:8080/volvo/taobao/app/special/20210706/api/tb/draw/draw'
        header = {
            'Content-Type': 'application/json',
            'openId': 'AAEm9hESANdAsZG-4d0TPDAl',
            'active_code': '3E053716241945BEA15ECB7539DFA13B'
        }
        data = {
            "oid": "string"
        }
        i = 1
        while i <= 10000:
            res = self.send_post(drawurl, data, header)
            success_res = res['success']
            respose = res['data']['res']
            if(success_res == True):
                result_json = respose['type']
                for key, val in MyTestCase.tinydict.items():
                    if (int(key) == result_json):
                        MyTestCase.tinydict[key] = val + 1
                MyTestCase.count = MyTestCase.count + 1
                self.assertTrue(success_res, msg='状态值不一致')
            i = i+1

    def test03(self):
        for k, v in MyTestCase.tinydict.items():
            avg = (v / MyTestCase.count) * 100
            if k == '1':
                p = '沃尔沃购物袋 '
            elif k == '2':
                p = '沃尔沃汽车定制棒球帽-白 '
            elif k == '3':
                p = '多功能商务背包 '
            elif k == '4':
                p = '随身杯-海精灵小号 '
            elif k == '5':
                p = '盲盒隐藏款（iphone13;戴森吹风机） '
            elif k == '6':
                p = '肩颈热敷电动按摩仪 '
            elif k == '7':
                p = '沃尔沃汽车定制XC90 儿童助步童车'
            elif k == '8':
                p = '无线充电动牙刷-黑/白'
            print('总抽奖人数为:%d ,抽中type为%s的次数为:%d,中奖概率为:%.2f%%' %
                  (MyTestCase.count, p, v, avg))


if __name__ == '__main__':
    suite1 = unittest.defaultTestLoader.discover(
        base_path, pattern='run*.py')
    # 创建测试报告输出地址
    file_path = base_path+'report.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,
                                                  title='测试报告',
                                                  description='volvo双十一抽奖概率！',
                                                  verbosity=2,
                                                  tester='小潘')
       # 执行测试用例，通过HTMLTestRunner的run()方法来运行测试套件中的测试用例
        runner.run(suite1)

    # 利用unittest中的TestSuite模块构造测试集
