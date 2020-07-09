import unittest
import time
from parameterized import parameterized
from PO1.page.page_calc import PageCalc
from PO1.base.get_driver import GetDriver
from PO1.tool.read_json import read_json


def get_data():
    datas = read_json('calc.json')
    arrs = []
    for data in datas.values():
        arrs.append((data['num1'], data['num2'], data['expect']))
    return arrs


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取driver
        cls.driver = GetDriver.get_driver()
        # 初始化计算页面对象
        cls.calc = PageCalc(cls.driver)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_calc(self, num1, num2, expect):
        self.calc.page_calc(num1, num2)
        print('预期结果为:%s, 实际结果为:%s' % (expect, self.calc.page_get_result()))
        try:
            self.assertEqual(self.calc.page_get_result(), str(expect))
        except AssertionError:
            self.calc.page_printscreen()