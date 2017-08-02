*** Settings ***
Library           Selenium2Library
Resource          公共关键字.robot
Resource          业务关键字.robot

*** Test Cases ***
创建订单
    管理员登录    admin    123456
    进入客户管理frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[2]/a    #点击订单
    Click Element    xpath=//*[@id='menuActions']/a    #创建订单
    sleep    3s
    Click Element    xpath=//*[@id='customer_chosen']/a    #点击客户
    Click Element    xpath=//*[@id='customer_chosen']/div/ul/li[2]    #选择zhaoyou
    Click Element    xpath=//*[@id='product_chosen']/ul    #点击产品
    Click Element    xpath=//*[@id='product_chosen']/div/ul/li[1]    #扫地机器人
    Select From List By Value    id=currency    usd    #选择美元
    Input Text    xpath=//*[@id='plan']    888
    Click Element    xpath=//*[@id='submit']    #点击保存按钮

删除订单
    管理员登录    admin    123456
    进入客户管理frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[2]/a    #点击订单
    sleep    3s
    Click Element    xpath=html/body/div[2]/div[2]/table/tbody/tr[1]/td[11]/div/a    #点击更多
    Click Element    xpath=html/body/div[2]/div[2]/table/tbody/tr[1]/td[11]/div/ul/li[4]/a    #点击删除
    Dismiss Alert
