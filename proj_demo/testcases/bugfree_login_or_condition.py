#!/user/bin/python
#encoding:utf-8

#__auth__=='__hq__'

import unittest
from selenium import webdriver
import time,os
from selenium.webdriver.support.ui import Select
import random
from config import *
from bussiness_common_steps import  *


class BugFreeLoginOrCondition(unittest.TestCase):
    """登录后查询或条件"""
    def setUp(self):
        self.executable_path = chrome_driver
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.url = "http://localhost/bugfree"
        open_url(self.driver,self.url)
        login_bugfree(self.driver,"admin","123456")

    def test_bugfree_bug1(self):
        """截图保存自定义显示视力"""
        driver=self.driver
        #driver.switch_to.window(driver.window_handles[0])

        driver.find_element_by_id("CustomSetLink").click()
        time.sleep(3)
        get_screenshot_immediately(driver)
        #点击确定按钮
        driver.find_element_by_xpath(".//*[@id='CustomSetTable']/tbody/tr[2]/td/input[1]").click()


    def test_bugfree_bug2(self):
        """下拉框多项选择"""
        driver = self.driver
        driver.find_element_by_link_text("Case").click()
        Select(driver.find_element_by_id("BugFreeQuery_andor1")).select_by_visible_text(u"或者")
        self.driver.find_element_by_id("SaveQuery").click()
        #这里有个问题：send_keys写死会弹出window窗口是否报错修改
        self.driver.find_element_by_id("dialogQueryTitle").send_keys("test_%s" % generate_random_num(1,99))
        time.sleep(2)
        get_screenshot_immediately(driver)
        self.driver.find_element_by_name("yt0").click()
        # 验证点，验证刚刚保存的查询是否出现在页面上
        driver.close()
    #
    def test_bugfree_bug3(self):
        """ +  -图标操作"""
        driver=self.driver
        driver.find_element_by_xpath(".//*[@id='SearchConditionRow0']/td[7]/a/img").click()
        time.sleep(2)
        get_screenshot_immediately(driver)
        driver.find_element_by_xpath(".//*[@id='SearchConditionRow1']/td[7]/a[2]/img").click()
        time.sleep(2)
        get_screenshot_immediately(driver)

    def tearDown(self):
        self.driver.quit()










