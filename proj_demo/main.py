#!/user/bin/env python
#encoding:utf-8

#__auth__=='__hq__'
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from testcases.bugfree_login_or_condition import BugFreeLoginOrCondition
from testcases.bugfree_import_file import BugfreeImportFile
from testcases.product_management.test_add_product import ProductAdd

def suites():
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    #suite.addTests(loader.loadTestsFromTestCase(BugFreeLoginOrCondition))
    #suite.addTests(loader.loadTestsFromTestCase(BugfreeImportFile))
    suite.addTests(loader.loadTestsFromTestCase(ProductAdd))
    #suite.addTests(loader.loadTestsFromTestCase(LoginLogoutTest))
    return suite

if __name__ == "__main__":
    suite = suites()
    fp = open('./reports/result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'Bugfree功能测试报告',
        description=u"测试用例执行情况：")
    runner.run(suite)
