import json
import requests
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)


class BaseRequests:
    def send_post(self, url, data, header):
        # 发送一个post请求
        response = requests.post(
            url=url, data=data, headers=header)
        res = response.json()
        # 返回res出去
        return res

    def login(self):
        login_url = 'http://192.168.3.17:8080/cn_gcc_sd10/tb/user/login'
        data = {
            "account": "378403323@qq.com",
            "loginType": 0,
            "password": "ziyouzhuyi"
        }
        # 将python数据结构转化为json
        data_json = json.dumps(data)
        login_header = {'Content-Type': 'application/json',
                        'token': 'ZdX5l9h+f+btpcydXYq8pT99ASimBKcMghZYRSHdo5jh1K3xUd3RxdAdLrDJX2ifH/ZEudNnx82Ya1l3WpRc0Sn+FyiQklyJoBAVrWGSfkBckvEoBDMeRbcZraBfdVcX'}
        self.send_post(login_url, data_json, login_header)

    def run_main(self, url, header):
        flag = 0
        count = 0
        if (flag == 0):
            self.login()
            flag += 1
            tinydict = {'0': 0, '1': 0, '2': 0, '3': 0,
                        '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
            while True:
                res = self.send_post(url, None, header)
                if(res['code'] == 0):
                    result_json = res['result']['type']
                    for key, val in tinydict.items():
                        if (int(key) == result_json):
                            tinydict[key] = val + 1
                    count = count+1
                elif (res['code'] == 504 or res['code'] == 503):
                    break
            for k, v in tinydict.items():
                avg = v/count*100
                print('总抽奖次数为:%d ,抽中type为%s的次数为:%d,中奖概率为:%.2f%%' %
                      (count, k, v, avg))


# 实例化类
request = BaseRequests()
if __name__ == "__main__":
    # 测试引入的host
    headers = {'token': 'ZdX5l9h+f+btpcydXYq8pT99ASimBKcMghZYRSHdo5jh1K3xUd3RxdAdLrDJX2ifH/ZEudNnx82Ya1l3WpRc0Sn+FyiQklyJoBAVrWGSfkBckvEoBDMeRbcZraBfdVcX'}
    request.run_main(
        'http://192.168.3.17:8080/cn_gcc_sd10/tb/draw/draw', headers)
