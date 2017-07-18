# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BugfreeNewCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bugfree_new_bug(self):
        driver = self.driver
        #新建1个case
        driver.find_element_by_link_text("Case").click()
        driver.find_element_by_link_text(u" 新建 Case   ").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id("CaseInfoView_title").clear()
        driver.find_element_by_id("CaseInfoView_title").send_keys("zwb003")
        driver.find_element_by_id("CaseInfoView_assign_to_name").click()
        driver.find_element_by_css_selector("li.ac_even").click()
        Select(driver.find_element_by_id("CaseInfoView_priority")).select_by_visible_text("2")
        Select(driver.find_element_by_id("Custom_CaseType")).select_by_visible_text(u"功能")
        Select(driver.find_element_by_id("Custom_CaseMethod")).select_by_visible_text(u"自动化脚本")
        driver.find_element_by_name("yt0").click()
        driver.close()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])

        #导航栏后退、前进操作
        #后退
        print "back to %s" % 'bug_page'
        driver.back()
        time.sleep(3)

        # 前进
        print "forword to %s" % 'case_page'
        driver.forward()
        time.sleep(3)

        # 截图
        self.driver.get_screenshot_as_file(r"C:\cap\bugfree_case_screen.jpg")


    def tearDown(self):
        # driver.find_element_by_link_text(u"退出").click()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
