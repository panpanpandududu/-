# 导入selenium包，webdriver是浏览器对象
from time import sleep

from selenium import webdriver
# 鼠标操作事件  导入动作链类（处理单击，双击，点击鼠标右键，拖拽等事件）
from selenium.webdriver.common.action_chains import ActionChains
# 键盘事件
from selenium.webdriver.common.keys import Keys

'''为了去除以下提示，特加入options
DevTools listening on ws://127.0.0.1:54427/devtools/browser/62c618e4-a3d4-48b5-a3e1-309b5a373d1b
[2816:14444:1123/175011.598:ERROR:device_event_log_impl.cc(211)] [17:50:11.598] Bluetooth: bluetooth_adapter_winrt.cc:1073 Getting Default Adapter failed.
'''

try:
    # 实例化谷歌浏览器
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    # 浏览器最大化
    driver.maximize_window()
    # 打开网址
    driver.get('https://www.jd.com')
    '''
    # id定位:定位搜索框，输入内容后回车，进行搜索
    search_element = driver.find_element_by_id("key")
    search_element.send_keys("平板电脑")
    sleep(2)
    # 点击回车进行搜索
    search_element.send_keys(Keys.RETURN)
    '''
    '''
    # class定位
    menu_item = driver.find_elements_by_class_name('cate_menu_lk')
    menu_item.click()
    '''
    '''
    # link_text定位
    #link_text = driver.find_element_by_link_text('手机')
    link_text = driver.find_element_by_partial_link_text('汽车用')
    link_text.click()
    '''
    '''
    # xpath定位
    xpath_file = driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li[2]/a[2]')
    xpath_file.click()
    '''
    '''
    # css选择器定位
    css_select = driver.find_element_by_css_selector(
        'li.cate_menu_item:nth-child(4) > a:nth-child(7)')
    css_select.click()
    '''
    '''鼠标键盘事件
    '''
    # 鼠标悬停
    # 停留在某个元素，可观察鼠标移动到元素上时的元素样式变化，最后调用perform()执行
    dbl = driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li[2]/a[1]')
    # 鼠标悬停并点击
    # ActionChains(driver).move_to_element(dbl).click(dbl).perform()
    # 鼠标悬停
    ActionChains(driver).move_to_element(dbl).perform()
    sleep(3)
    old_phone = driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/dl[1]/dd/a[6]')
    ActionChains(driver).move_to_element(old_phone).click(old_phone).perform()

finally:
    sleep(3)
    driver.quit()
