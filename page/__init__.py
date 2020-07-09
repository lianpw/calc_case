from selenium.webdriver.common.by import By

# 环境url地址
url = 'http://cal.apple886.com/'

"""以下为计算器配置数据"""
# 数字键
# calc_num = By.CSS_SELECTOR, ''

# 加号
calc_add = By.CSS_SELECTOR, '#simpleAdd'

# 等号
calc_equal = By.CSS_SELECTOR, '#simpleEqual'

# 获取结果
calc_result = By.CSS_SELECTOR, '#resultIpt'

# 清屏
calc_clear = By.CSS_SELECTOR, '#simpleClearAllBtn'