# 代码运行需要python环境，安装所需模块
建议pycharm 

https://www.jetbrains.com/pycharm/download/#section=windows 

选择Community

安装完python后在终端下输入 

pip install bs4 

pip install lxml

pip install requests

也可以使用pyinstaller直接生成打卡exe文件（输入学号，密码后）
# 在郑州大学打卡（2）中输入学号，密码
学号 20xxxxxxxx
密码 身份证后八位或教务系统密码
# 代码运行会在当前目录形成打卡成功的网页
生成daka.html![daka](https://user-images.githubusercontent.com/99618903/176407649-a790a95a-7b76-457c-aaa9-b21e28253893.png
# 打卡次数有限制
次数过多会导致输入验证码，打卡会不成功（输入验证码的功能可以实现，但没必要）
等待一段时间就行
# 设置自动打卡
可以在自己电脑上，也可以在云服务器上（保证永不关机，否则只会在开机时运行）

搜索任务计划程序 

创建任务 

 选择最高权限运行（可以黑屏运行）
 
 触发器时间选择最好定两个时间23：58，0：30 刚过0点会网络拥堵，实际上打卡系统会在23点50左右刷新
 
 操作选择启动程序浏览选择 郑州大学打卡2.0.py
 
 
 # 代码失效
 代码失效大概率原因为填报的信息变化，可以通过编辑 郑州大学打卡2.0.py中的data2词典来使其重新生效
 
 具体填报信息可以通过抓包获得
 
 在edge浏览器登陆打卡系统填报页面下右击鼠标，检查，右边窗口选择网络，打卡系统进行填报，选择jksb选项，负载（payload）。
 
 将此项所有信息与郑州大学打卡2.0.py的data2信息保持一致。
 
https://user-images.githubusercontent.com/99618903/176416870-6645d39a-722d-4ecb-9937-729e07e289fa.mp4
# 关于郑州大学打卡.py
不知道为何失效
