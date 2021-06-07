
import requests


class BaseRequests:
    # 定义一个post方法
    def send_post(self, url, data, header):
        # 发送一个post请求
        response = requests.post(
            url=url, data=data, headers=header)
        res = response.json()
        # 返回res出去
        return res


BaseRequests = BaseRequests()
