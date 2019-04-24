# wechatRobot
微信聊天机器人DIY版

基于Python2 itchat实现的微信机器人

## 0x00环境安装
首先安装python环境  

然后需要安装依赖库 

pip  install itchat  requests

## 0x01 DIY修改

代码中nickName为机器人名称     
phoneNumber为开发者的联系方式  
可以DIY修改   

此处调用了图灵机器人的接口，需要到[图灵机器人](http://www.tuling123.com)官网注册账号  
新建机器人，获取其apikey的值（十六进制的字符串），然后填入50行处的key的后面。  
"key":"XXXXXXXXXXXXXXXXXXXXXXX",此处XXXXXXXXXXX修改为自己机器人apikey值

## 0x02 使用
修改完毕后 使用
python itrobot.py 开启机器人，然后手机扫描登录确认，就完成了微信聊天机器人。

