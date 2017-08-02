*** Settings ***
Library           Selenium2Library
Resource          业务关键字.robot
Resource          公共关键字.robot

*** Test Cases ***
管理员登录退出
    [Setup]
    [Template]
    管理员登录    admin    123456
    管理员退出
    [Teardown]

*** Keywords ***
