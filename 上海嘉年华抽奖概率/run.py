
from handle_excel import excel_data
import random
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
base_path = os.getcwd() + '/抽奖概率/上海嘉年华抽奖概率'
sys.path.append(base_path)

# Excel数据
datas = excel_data.get_excel_data()


@ddt.ddt
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
        t1 = list(range(1, 9))
        t2 = [0] * 8
        MyTestCase.tinydict = dict(zip(t1, t2))
        MyTestCase.count = 0

    @ ddt.data(*datas)
    @ ddt.unpack
    def test02(self, uid):
        drawurl = 'http://car.velo.com.cn/r/draw/20210625/api/tb/draw/draw'

        header = {
            'Content-Type': 'application/json',
            'uid': str(uid)
        }
        res = self.send_post(drawurl, None, header)
        status = res['code']
        respose = res['res']
        if(status == 0):
            result_json = respose['iid']
            for key, val in MyTestCase.tinydict.items():
                if (key == result_json):
                    MyTestCase.tinydict[key] = val + 1
            MyTestCase.count = MyTestCase.count + 1
            self.assertEqual(0, status, msg='状态值不一致')

    def test03(self):
        gifts = ['感谢参与 ', '盲盒 ', 'R汽车 定制环保袋 ', '冰淇淋',
                 'R汽车 定制扇子 ', '免费上门试驾服务 ', '半夏 键盘套装 ', '周杰伦 签名照 ']
        for k, v in enumerate(MyTestCase.tinydict):
            avg = (v / MyTestCase.count) * 100
            for index, value in enumerate(gifts):
                if (k == index):
                    print('总抽奖人数为:%d ,抽中type为%s的次数为:%d,中奖概率为:%.2f%%' %
                          (MyTestCase.count, value, v, avg))


if __name__ == '__main__':

    suite1 = unittest.defaultTestLoader.discover(
        base_path, pattern='run*.py')
    # 创建测试报告输出地址
    file_path = base_path+'report.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,
                                                  title='测试报告',
                                                  description='上海嘉年华抽奖概率的测试报告！',
                                                  verbosity=2,
                                                  tester='小潘')
       # 执行测试用例，通过HTMLTestRunner的run()方法来运行测试套件中的测试用例
        runner.run(suite1)

    # 利用unittest中的TestSuite模块构造测试集
