import unittest
r1 = range(1, 3)
""" r2 = range(1, 3)
for i in r1:
    print("我是外循环")
    for j in r2:
        print("我是内循环")
        print('i= %d,j=%d' % (i, j)) """
# 总结：外层循环执行一次，内层循环全部执行一遍;如果外层循环需要执行m次，内层循环需要执行n次，嵌套循环一共执行mxn次

""" r3 = range(1, 6)
for i in r3:
    for j in r3:
        print('*', end='')
    print() """
""" 包含end=''作为print()BIF的一个参数，会使该函数关闭“在输出中自动包含换行”的默认行为。其原理是：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。这个只有Python3有用，Python2不支持 """

""" for...in... 循环
可遍历字符串，列表，元祖，字典 """
# 遍历字符串
# s = 'do you like eat meal'
# print(len(s))
# for i in s:
#     print(i)


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Login.tinydict = {'1': 0, '2': 0, '3': 0, '4': 0,
                          '5': 0, '6': 0, '7': 0}
        Login.count = 0

    def test_1(self):
        for key, val in Login.tinydict.items():
            Login.tinydict[key] = val + 1
            Login.count = Login.count + 1
            print(Login.tinydict)  # 打印：test_1中：333

    def test_2(self):
        print(Login.count)  # 打印：test_2中：333


if __name__ == '__main__':
    unittest.main()
