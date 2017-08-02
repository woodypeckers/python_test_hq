*** Settings ***
Library           Selenium2Library
Resource          公共关键字.robot
Resource          业务关键字.robot

*** Test Cases ***
新增冰箱产品
    管理员登录    admin    123456
    进入客户管理frame
    Click Element    //*[@id='mainNavbar']/div[2]/ul/li[7]/a    #产品
    Click Element    //*[@id='menuActions']/a    #添加产品
    sleep    1s
    Input Text    xpath=//*[@id='name']    冰箱    #输入产品
    Input Text    xpath=//*[@id='code']    bingxiang    #输入代号
    Select From List By Index    xpath=//*[@id='status']    002    #选择产品线下拉框
    Click Element    xpath=//*[@id='submit']    real    #选择实体类

新增冰箱产品线
    管理员登录    admin    123456
    进入客户管理frame
    Click Element    //*[@id='mainNavbar']/div[2]/ul/li[7]/a
    Click Element    html/body/div[2]/div[2]/div[1]/div[2]/a
    Sleep    1s
