# Automatic-ZYTX-METAR-Message-System
It is a system that can get METAR messages of ZYTX airport and push the METAR message to Wechat through WXPusher.
软件名称：沈阳桃仙机场METAR报文自动推送程序
版本号：2024.07.28
软件版权归属：吴瀚庆
未经允许，禁止盗用，侵权必究

有意请联系软件作者 吴瀚庆
微信：whq20050121
手机：19528873640
邮箱：m19528873640@outlook.com
欢迎提出宝贵意见，感谢支持！

更新日志：
2024.05.21	程序诞生，通过爬取https://www.flightaware.com/live/airport/ZYTX，然后对爬取到的信息进行处理
			通过WXPusher推送到关注了“ZYTX_METAR”程序的用户
2024.05.25	完善了一下对于datetime_list列表长度的控制，控制在4个元素以内，控制内存
2024.05.26	完善了一下write_error_log()函数的功能，使得不但可以输出报错，而且可以将报错信息推送到管理员，管理员的uid储存在uid_list_admin
2024.05.28	完善了get_metar_list()函数的报错以及等待，使用了selenium的显式等待，而不再采用time.sleep()等待的方式
			增加了版本号的显示，软件界面中显示版本号，以及推送消息时也显示版本号
2024.06.15	修改了get_metar_list()函数的逻辑，加入了try...except和while循环
			完善了爬取数据时处理报错的能力，比如遇到网络超时等问题，不会结束函数，而是就等待数秒钟后重新爬取数据
2024.06.19	完善了报错日志内容，在报错日志中添加了设备名称以及版本号的信息
2024.07.22	新增了release()函数，用于每次循环结束后，删除变量，释放内存
2024.07.28	修改了user_agents的获取，取消了通过fake_useragent库动态获取模拟请求头，而是通过读取txt获取请求头
			避免因fake_useragent库引发的打包错误问题

软件使用注意：
请勿擅自动软件目录下的任何txt文件！！！

使用方法：（暂无）


软件源码简单说明：（暂无）


关于软件说明，就到此为止啦~
欢迎提出宝贵意见，感谢支持！

