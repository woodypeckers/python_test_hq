*** Settings ***
Library           Selenium2Library
Resource          业务关键字.robot
Resource          公共关键字.robot

*** Test Cases ***
添加联系人
    管理员登录    admin    123456
    进入客户管理frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[5]/a    #联系人
    Sleep    1s
    Click Element    xpath=//*[@id='menuActions']/a    #添加联系人
    Input Text    xpath=//*[@id='realname']    wenbo    #输入真实姓名
    Click Element    xapth=//*[@id='menuActions']/a    #点击
    Click Element    xpath=//*[@id='newCustomer']    wenbo    #所属用户
    ${mytime}=    Get Time
    Input Text    xpath=//*[@id='name']
    Click Element    xpath=//*[@id='submit']
