*** Settings ***
Library           Selenium2Library
Resource          公共关键字.robot

*** Keywords ***
管理员登录
    [Arguments]    ${username}    ${password}
    打开登录页面
    输入用户名    ${username}
    输入密码    ${password}
    点击登录按钮
    Sleep    3s

管理员退出
    点击签退
