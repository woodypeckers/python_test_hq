#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BugFreeProduct_01(unittest.TestCase):
    """登录BUGFREE操作，前进后退"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def add_product(self):
        """下拉框选择，跳转窗口，有个疑问的地方，TypeError: 'Alert' object is not callable"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        time.sleep(3)
        driver.find_element_by_id("LoginForm_rememberMe").click()
        time.sleep(3)
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.find_element_by_link_text(u"后台管理").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_link_text(u"添加产品").click()
        time.sleep(2)
        driver.find_element_by_id("Product_name").clear()
        driver.find_element_by_id("Product_name").send_keys("product_006")
        driver.find_element_by_id("Product_display_order").clear()
        driver.find_element_by_id("Product_display_order").send_keys("100")
        driver.find_element_by_id("Product_product_manager").click()
        driver.find_element_by_xpath("html/body/div[3]/ul/li").click()
        time.sleep(3)
        driver.find_element_by_id("Product_bug_severity").clear()
        driver.find_element_by_id("Product_bug_severity").send_keys("2")
        driver.find_element_by_id("Product_bug_priority").send_keys("1,2,3,4")
        driver.find_element_by_id("Product_case_priority").clear()
        driver.find_element_by_id("Product_case_priority").send_keys("3")
        driver.find_element_by_xpath("//*[@id='product-form']/div[9]").location
        driver.find_element_by_xpath("//*[@id='product-form']/div[9]").send_keys(u"你好")
        time.sleep(2)
        #driver.find_element_by_xpath("//*[@id='product-form']/div[9]/div/div/div[1]/span[33]/span").click()
        #time.sleep(3)
        #driver.switch_to.alert().accept()
        #driver.find_element_by_class_name("ke-button-common ke-button").click()
        #time.sleep(3)
        #driver.switch_to.alert().accept()
        #driver.find_element_by_xpath("//*[@id='product-form']/div[9]").location
        #link = driver.find_element_by_xpath("//*[@id='product-form']/div[9]/div/div/div[1]/span[10]/span")
        #ActionChains(driver).move_to_element(link).click()
        #time.sleep(2)
        #driver.find_element_by_xpath("//*[@id='product-form']/div[10]/label").location
        #driver.find_element_by_class_name("ke-content").send_keys(u"1.用户步骤\n2.预置备件\n3.期望输出")
        driver.find_element_by_id("Product_is_dropped").click()
        driver.find_element_by_xpath("//option[@value='1']").click()
        #driver.find_element_by_xpath("//input[contaims(@value,'1')]").click()
        time.sleep(3)
        driver.find_element_by_name("yt0").click()
        driver.get_screenshot_as_file(r"F:\picture\product_screen_jpg")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        #driver.find_element_by_link_text(u"退出").click()

class BugFreeBug_01(BugFreeProduct_01):

    def add_bug(self):
        """点击浏览后，弹出的新窗口，没能关闭，只是用了switch_to_window(driver.window_handles[1])跳过此步骤"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='create_div']/a").click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id("BugInfoView_title").send_keys(u"这个输入错误，不合理")
        driver.find_element_by_id("BugInfoView_assign_to_name").click()
        driver.find_element_by_xpath("html/body/div[4]/ul/li").click()
        driver.find_element_by_xpath("//*[@id='BugInfoView_mail_to']").click()
        driver.find_element_by_xpath("html/body/div[5]/ul/li").click()
        driver.find_element_by_xpath("//*[@id='BugInfoView_severity']").click()
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_xpath("//*[@id='BugInfoView_priority']").click()
        time.sleep(3)
        #driver.find_element_by_id("attachment_file").click() 点击浏览弹出来的新窗口，如何处理
        #driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_xpath("//*[@id='buttonlist']/input[1]").click()
        driver.switch_to.window(driver.window_handles[0])
        #连接点击三次，然后选择下拉框查询
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='SearchConditionRow0']/td[7]/a/img").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='BugFreeQuery_field1']").click()
        driver.find_element_by_xpath("//option[@value='module_name']").click()
        driver.find_element_by_xpath("//*[@id='BugFreeQuery_operator1']").click()
        driver.find_element_by_xpath("//option[@value='>']").click()
        driver.find_element_by_id("PostQuery").click()
        driver.get_screenshot_as_file("F:\picture\screen001_jpg")
        driver.find_element_by_link_text("退出").click()

if __name__ == "__main__":
    suit = unittest.TestSuite()
    loader = unittest.TestLoader()
    suit.addTests(loader.loadTestsFromTestCase("BugFreeProduct_01,BugFreeBug_01"))

    fp = open("./test_result_%s.html" % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        tile=u'bugfree测试报告',
        description=u"测试用例执行情况：")
    runner.run(suit)
    fp.close()
