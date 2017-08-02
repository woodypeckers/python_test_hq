*** Settings ***
Library           Selenium2Library

*** Variables ***
${open_url}       http://localhost/ranzhi/www
${title}          然之协同
${username}       admin
${password}       123456

*** Keywords ***
打开登录页面
    Open Browser    ${open_url}    Chrome

输入用户名
    [Arguments]    ${username}
    Input Text    id=account    ${username}

输入密码
    [Arguments]    ${password}
    Input Password    id=password    ${password}
    Sleep    1s

点击登录按钮
    Click Button    id=submit
    Sleep    3s
    Page Should Contain    ${title}
    sleep    3s

点击签退
    Click Button    id=start
    sleep    3s
    Click Link    xpath=.//*[@id='startMenu']/li[10]/a
    sleep    3s

进入客户管理frame
    Click Element    xpath=//*[@id='s-menu-1']/button    #点击客户管理
    Select Frame    id=iframe-1
