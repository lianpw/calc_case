from selenium.webdriver.common.by import By
from PO1.base.base import Base
from PO1 import page


class PageCalc(Base):
    # 点击数字方法
    def page_click_num(self, num):
        for i in str(num):
            calc_num = By.CSS_SELECTOR, '#simple{}'.format(i)
            self.base_click(calc_num)

    # 点击加号
    def page_add(self):
        self.base_click(page.calc_add)

    # 点击等号
    def page_eq(self):
        self.base_click(page.calc_equal)

    # 获取结果
    def page_get_result(self):
        return self.base_input_value(page.calc_result)

    # 点击清屏
    def page_click_clear(self):
        self.base_click(page.calc_clear)

    # 截图方法
    def page_printscreen(self):
        self.base_printscreen()

    # 组合业务方法
    def page_calc(self, num1, num2):
        self.page_click_num(num1)
        self.page_add()
        self.page_click_num(num2)
        self.page_eq()