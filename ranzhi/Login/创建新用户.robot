*** Settings ***
Library           Selenium2Library
Resource          业务关键字.robot
Resource          公共关键字.robot

*** Test Cases ***
创建新用户王武
    管理员登录    admin    123456
    Click Element    //*[@id='s-menu-superadmin']/button    #点击后台管理
    sleep    3s
    select frame    name=iframe-superadmin
    Click Element    //*[@id='shortcutBox']/div/div[1]/div/a/h3    #点击添加成员
    sleep    3s
    Input Text    //*[@id='account']    wangwu
    Input Text    //*[@id='realname']    王武
    sleep    3s
    #Click Element    //*[@id='gender1']    \    #性别男
    Select From List By Value    //*[@id='role']    sale    #销售
    Input Password    //*[@id='password1']    123456    #输入密码
    Input Password    //*[@id='password2']    123456    #重复输入密码
    Input Text    //*[@id='email']    254302410@qq.com    #请输入邮箱号
    Click Element    //*[@id='submit']    #点击保存按钮

新用户王武登录
    管理员登录    wangwu    123456
