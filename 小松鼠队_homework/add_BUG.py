# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddProduct20170709(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_product20170709(self):
        """点击浏览后，弹出的新窗口，没能关闭，只是用了switch_to_window(driver.window_handles[1])跳过此步骤"""
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

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suit = unittest.TestSuite()
    loader = unittest.TestLoader()
    suit.addTests(loader.loadTestsFromTestCase(AddProduct20170709))

    fp = open("./test_result_%s.html"% time.strftime("%Y-%m-%d %H-%M-%S"),'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'bugfree报告',
        description=u"测试用例执行情况：")
    runner.run(suit)
    fp.close()
