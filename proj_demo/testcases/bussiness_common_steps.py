#!/user/bin/env python
#encoding:utf-8
#__auth__=='__hq__'

import time

def open_url(driver,url):
    driver.get(url)

def login_bugfree(driver,username,password):
    driver.find_element_by_id("LoginForm_username").clear()
    driver.find_element_by_id("LoginForm_username").send_keys(username)
    driver.find_element_by_id("LoginForm_password").clear()
    driver.find_element_by_id("LoginForm_password").send_keys(password)
    driver.find_element_by_id("SubmitLoginBTN").click()

def click_element_by_id_with_sleep(driver,id,sleep=2):
    #判断元素是否存在
    try:
        driver.find_element_by_id(id).click()
    except:
        pass
    finally:
        time.sleep(2)

def input_filename_click_ok():
    import os
    cur_dir = os.getcwd()
    print cur_dir
    os.system("%s/tools/upload_file_x64.exe" % cur_dir)

def get_screenshot_immediately(driver,path=None):
    """截图，保存路径"""
    if path is None:
        driver.get_screenshot_as_file(r"./screenshots/shots_%s.jpg" % time.strftime("%Y-%m-%d %H-%M-%S"))
    else:
        driver.get_screenshot_as_file(path)

def generate_random_num(start,stop):
    """
    @desc：生成一个随机函数，根据传入的起始，返回一个之间的数
    @usage:generate_random_num(1,99)
    """
    import random
    return random.randint(start,stop)








