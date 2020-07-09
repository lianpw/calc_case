import time
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 获取value属性值方法
    def base_input_value(self, loc):
        return self.base_find_element(loc).get_attribute('value')

    # 截图
    def base_printscreen(self):
        self.driver.get_screenshot_as_file('../img/{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))