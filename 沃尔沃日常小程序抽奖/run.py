import random
import time
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
base_path = os.getcwd() + '/抽奖概率/沃尔沃日常小程序抽奖'
sys.path.append(base_path)


class MyTestCase(unittest.TestCase):
    def send_post(self, url, data, header):
        # 发送一个post请求
        # 在request.get()\requet.post()里面加参数：verify=False；目的是：移除SSL认证；此时，fiddler就可以抓取到python-requets 请求的包了
        response = requests.post(
            url=url, data=json.dumps(data), headers=header, verify=False)
        res = response.json()
        # 返回res出去
        return res

    @classmethod
    def setUpClass(cls):
        t1 = ['杯子', '手机支架', '水', '定制卫衣',
              '定制雨伞', '周杰伦专辑', '奖品7', '奖品8']
        t2 = [0] * 8
        MyTestCase.tinydict = dict(zip(t1, t2))
        MyTestCase.count = 0

    def test02(self):  # 设置默认时间间隔和超时时间
        drawurl = 'http://39.99.252.209:8080/volvo/taobao/app/usual/20210922/api/tb/draw/draw'
        header = {
            'Content-Type': 'application/json',
            'openid': 'AAEIP08rANv6Cwxlf7qVP2WK',
            'active_code': "122"
        }
        data = {
            "oid": "1635924405190"
        }

        i = 1
        while i <= 1000:
            res = self.send_post(drawurl, data, header)
            status = res['data']['code']
            respose = res['data']['res']
            if(status == 0):
                result_json = respose['name']
                for key, val in MyTestCase.tinydict.items():
                    if (key == result_json):
                        MyTestCase.tinydict[key] = val + 1
                MyTestCase.count = MyTestCase.count + 1
                self.assertEqual(0, status, msg='状态值不一致')
            i = i+1

    def test03(self):
        for k, v in MyTestCase.tinydict.items():
            avg = (v / MyTestCase.count) * 100
            print('总抽奖人数为:%d ,抽中type为%s的次数为:%d,中奖概率为:%.2f%%' %
                  (MyTestCase.count, k, v, avg))


if __name__ == '__main__':

    suite1 = unittest.defaultTestLoader.discover(
        base_path, pattern='run*.py')
    # 创建测试报告输出地址
    file_path = base_path+'/report.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,
                                                  title='测试报告',
                                                  description='沃尔沃日常抽奖概率的测试报告！',
                                                  verbosity=2,
                                                  tester='小潘')
       # 执行测试用例，通过HTMLTestRunner的run()方法来运行测试套件中的测试用例
        runner.run(suite1)

    # 利用unittest中的TestSuite模块构造测试集
