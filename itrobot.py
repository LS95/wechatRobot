#!/usr/bin/env python
#coding=utf-8
import itchat
import time
import  requests
import  json
import  thread


nickName= u"your name" # 此处修改为您的昵称
phoneNumber = u"1XXXXXXXXXX" # 此处修改为您的联系方式
newInstance = itchat.new_instance()

# 获取当前时间
def getCurrrentSystemTime():
     currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) # 格式化时间，按照 2017-04-15 13:46:32的格式打印出来
     return currentTime
# 判读是否是工作时间  23:00-6:00
def isWorkTime():
    currentHour = time.strftime('%H', time.localtime())
    intHour = int(currentHour)
    if   (intHour >=0 and intHour <=6) or (intHour == 23):
        return True
    return False

@newInstance.msg_register('Text')
def text_reply(msg):
    if(msg.text.lower() == ("help")):
        return  u"[主人暂时不在，我是{}1号-help]\n输入信息 我们就可以愉快的聊天啦~\n 获取联系方式请回复phone \n例如:北京天气\n讲个笑话\n故事来一个\n......".format(nickName)
    elif (msg.text.startswith("phone")):
        return  u"[主人暂时不在，我是{}]\n悄悄的告诉你我爸爸的电话是{}:\n\n一般人我不告诉他~\n".format(nickName,phoneNumber)
    elif  (msg.text.startswith("lt") or u"聊天" in msg.text):
        inputMsg = msg['Text'][2:]
        responseMsg = tulin_robot(inputMsg)
        return  u"[主人暂时不在，我是{}3号-debug]\n{}".format(nickName,responseMsg)
    else:
        current_time = time.localtime(time.time())
        #定时发送销售
        if((current_time.tm_sec % 5 == 0)):
            replay = u'时间: %s' % (getCurrrentSystemTime()) 
            newInstance.send(replay, toUserName="filehelper")
        inputMsg = msg['Text']
        responseMsg = tulin_robot(inputMsg)
        return  u"[主人暂时不在，我是{}]\n{}".format(nickName,responseMsg)


def  tulin_robot(text):
    url="http://www.tuling123.com/openapi/api"
    data={
        "key":"XXXXXXXXXXXXXXXXXXXXXXX",#此处修改为自己机器人apikey值
        "info":text,#从微信传输过来的文本内容
        'userid': 'wechat-robot',
        'loc':"北京"
    }
    r=requests.post(url,data=data).json()
    code=r["code"]
    """100000  文本类
       200000  链接类
       302000  新闻类
       308000  菜谱类
       313000  儿歌类
       314000  诗词类"""
    if  code==  302000:
        result = ''
        allNews = r["list"]
        for each in allNews:
            result = result + each["article"] + "\n" + each["detailurl"]
            result = result + "\n***********************\n"
        return   "%s\n%s" %(r["text"],result)
    if code==  100000:
        return  r["text"]
    if   code==200000:
        return "%s %s" %(r["text"],r["url"])
    if   code==313000:
        return  "%s %s %s" %(r["text"],r["function"]["song"],r["function"]["singer"])
    if   code==314000:
        return  "%s %s %s" %( r["text"],r["function"]["author"],r["function"]["name"])
    if   code==308000:
        result = ''
        allNews = r["list"]
        for each in allNews:
            result = result + each["name"] + "\n" + each["info"] +"\n" + each["detailurl"]
            result = result + "\n***********************\n"
        return   "%s\n%s" %(r["text"],result)

def sendTask():
    while True:
        current_time = time.localtime(time.time())
        #定时发送销售
        if((current_time.tm_hour %1 == 0) and (current_time.tm_min %30 == 0) and (current_time.tm_sec == 0)):
            replay = u'时间: %s' % (getCurrrentSystemTime()) 
            itchat.send(replay, toUserName="filehelper")
        time.sleep(1)

def lc():
    print('finish login')
    itchat.send(u'机器人上线 %s' % getCurrrentSystemTime(), toUserName='filehelper')#发送内容

def ec():
    print('exit')
    itchat.send(u'机器人下线 %s ' % getCurrrentSystemTime(), toUserName='filehelper')#发送内容


newInstance.auto_login(enableCmdQR=2,hotReload=True, statusStorageDir="newInstance.pkl")


try:
    newInstance.run(debug=True)
except:
    itchat.logout()

