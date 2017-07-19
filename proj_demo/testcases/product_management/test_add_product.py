#!/user/bin/env python
#encoding:utf-8

#__auth__=='__hq__'
import unittest
import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from config import *
from testcases.bussiness_common_steps import  *
from selenium.webdriver.support.ui import Select
import random

class ProductAdd(unittest.TestCase):
    def setUp(self):
        self.executable_path = chrome_driver
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.url = "http://localhost/bugfree"
        open_url(self.driver,self.url)
        login_bugfree(self.driver,"admin","123456")

    def test_product001(self):
        """添加产品"""
        driver = self.driver
        driver.find_element_by_link_text(u"导入").click()
        driver.find_element_by_id("casefilename").click()
        time.sleep(2)
        cur_dir = ("F:/gihub_case/proj_demo/tools")
        print cur_dir
        os.system("%s/upload_file_x64.exe" % cur_dir)
        driver.find_element_by_id("uploadbutton").click()
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        driver.find_element_by_link_text(u"后台管理").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_link_text(u"添加产品").click()
        driver.find_element_by_id("Product_name").clear()
        self.product_id = "Product_%s" % generate_random_num(1, 99)
        driver.find_element_by_id("Product_name").send_keys(self.product_id)
        driver.find_element_by_id("Product_display_order").clear()
        driver.find_element_by_id("Product_display_order").send_keys("100")
        time.sleep(2)
        #点击产品管理员下拉框
        driver.find_element_by_xpath(".//*[@id='Product[group_name][]']/span").click()
        #点击all user
        driver.find_element_by_xpath(".//*[@id='product-form']/div[4]/div/label[2]").click()
        time.sleep(3)
        driver.find_element_by_id("Product_bug_severity").clear()
        driver.find_element_by_id("Product_bug_severity").send_keys("2")
        driver.find_element_by_id("Product_bug_priority").send_keys("1,2,3,4")
        driver.find_element_by_id("Product_case_priority").clear()
        driver.find_element_by_id("Product_case_priority").send_keys("1,2,3,4")
        time.sleep(2)
        driver.find_element_by_name("yt0").click()

    def tearDown(self):
        # 删除掉刚刚生成的产品id,   self.product_id
        # 连接到数据库之后，执行delete 语句
        pass

