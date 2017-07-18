#!/user/bin/python
#encoding:utf-8

#__auth__=='__hq__'

import unittest
from selenium import webdriver
import os, time
from bussiness_common_steps import *
from config import *


class BugfreeImportFile(unittest.TestCase):
    def setUp(self):
        self.executable_path = chrome_driver
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.url = "http://localhost/bugfree"
        open_url(self.driver,self.url)
        login_bugfree(self.driver,"admin","123456")

    def tearDown(self):
        self.driver.quit()

    def test_bugfree_bug2(self):
        """测试导入文件的功能"""
        driver = self.driver
        driver.find_element_by_link_text(u"导入").click()

        #打开选择文件对话框，然后选择文件，最后点击确定
        click_element_by_id_with_sleep(driver,"casefilename")
        input_filename_click_ok()
        get_screenshot_immediately(driver)
        #点击“导入”按钮
        click_element_by_id_with_sleep(driver,"uploadbutton")
        driver.switch_to.alert.accept()
        get_screenshot_immediately(driver)