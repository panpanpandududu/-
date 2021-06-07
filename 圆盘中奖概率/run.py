
from handle_excel import excel_data
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
base_path = os.getcwd()+'/圆盘中奖概率'
sys.path.append(base_path)

# Excel数据
datas = excel_data.get_excel_data()


@ddt.ddt
class MyTestCase(unittest.TestCase):
    def send_post(self, url, data, header):
        # 发送一个post请求
        # 在request.get()\requet.post()里面加参数：verify=False；目的是：移除SSL认证；此时，fiddler就可以抓取到python-requets 请求的包了
        response = requests.post(
            url=url, data=data, headers=header, verify=False)
        res = response.json()
        # 返回res出去
        return res

    @ddt.data(*datas)
    @ddt.unpack  # 分解参数
    def test01(self, username, phone, carType, openId):
        # Headers配置
        header = {
            'Content-Type': 'application/json',
            'openId': openId
        }
        loginurl = 'https://car.velo.com.cn/r/show/20210401/api/tb/base/submit'
        data = {
            "carType": carType,
            "name": username,
            "phone": phone
        }
        data_json = json.dumps(data)
        res = self.send_post(loginurl, data_json, header)
        status = res['code']
        self.assertEqual(0, status, msg='状态值不一致')

    # @classmethod
    # def setUpClass(cls):
    #     MyTestCase.tinydict = {'1': 0, '2': 0, '3': 0, '4': 0,
    #                            '5': 0, '6': 0, '7': 0}
    #     MyTestCase.count = 0

    # @ddt.data(*datas)
    # @ddt.unpack
    # def test02(self, openId):
    #     drawurl = 'https://car.velo.com.cn/r/show/20210401/api/tb/draw/draw'
    #     header = {
    #         'Content-Type': 'application/json',
    #         'openId': openId
    #     }
    #     res = self.send_post(drawurl, None, header)
    #     if(res['code'] == 0):
    #         result_json = res['res']['type']
    #         for key, val in MyTestCase.tinydict.items():
    #             if (int(key) == result_json):
    #                 MyTestCase.tinydict[key] = val + 1
    #         MyTestCase.count = MyTestCase.count + 1
    #         self.assertEqual(0, res['code'], msg='状态值不一致')

    # def test03(self):
    #     for k, v in MyTestCase.tinydict.items():
    #         avg = (v/MyTestCase.count)*100
    #         print('总抽奖人数为:%d ,抽中type为%s的次数为:%d,中奖概率为:%.2f%%' %
    #               (MyTestCase.count, k, v, avg))


if __name__ == '__main__':
    unittest.main()
    # 识别测试用例

    # suite1 = unittest.defaultTestLoader.discover(
    #     base_path, pattern='run*.py')
    # # 创建测试报告输出地址
    # file_path = base_path+'report04.html'
    # with open(file_path, 'wb') as f:
    #     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,
    #                                               title='测试报告',
    #                                               description='这是第3次执行接口概率用例的测试报告！',
    #                                               verbosity=2,
    #                                               tester='小潘')
    #    # 执行测试用例，通过HTMLTestRunner的run()方法来运行测试套件中的测试用例
    #     runner.run(suite1)
