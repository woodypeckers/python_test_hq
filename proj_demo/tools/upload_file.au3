;获取窗口句柄
$handle = WinGetHandle("打开")
WinActivate($handle)
;获取控件句柄

;选择要上传的文件
AutoItSetOption("SendKeyDelay",30)
Send("F:\gihub_case\proj_demo\tools\buglist.xml")

;确认选择
Send("{ENTER}")