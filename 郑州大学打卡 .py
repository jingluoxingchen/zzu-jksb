import requests
import bs4
import lxml

useragent= 'Mozilla/5.0 (Linux; Android 11; MI 6 Build/RKQ1.200826.002;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36'
def login():
    headers={
        'User-Agent':useragent,
    }
    data={
        'uid':'20xxxxxxxxx',#学号
        'upw':'xxxxxxxx.',#身份证后八位或教务系统密码
        'smbtn': '进入健康状况上报平台',
        'hh28': '701',
    }
    url= 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0'
    loginurl='https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'

    requests.get(url=url,data=data,headers=headers)
    res=requests.post(url=loginurl,headers=headers,data=data)
    res.encoding = 'utf-8'
    res=res.text
    soup=bs4.BeautifulSoup(res,'lxml')
    jkl=soup.find('script').string
    list=jkl.split('n=')
    newurl=list[-1].split('"')[1]
    requests.post(url=newurl,headers=headers,data=data)
    list1 = newurl.split('id=')
    piopid = list1[1].split('&')[0]
    sid = list1[2].split('&')[0]
    return piopid,sid
login()
list=list(login())
piopid=list[0]
sid=list[1]
def jksb():
    url='https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb'
    headers = {
        'User-Agent': useragent
    }
    data={
        'did': '1',
        'door':'',
        'men6': 'a',
        'ptopid':piopid,
        'sid':sid
    }
    ty=requests.post(url=url,headers=headers,data=data)
def jksb2():
    url = 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb'
    headers = {
        'User-Agent': useragent
    }
    data={'myvs_1': '否',
        'myvs_2': '否',
        'myvs_3': '否',
        'myvs_4': '否',
        'myvs_5': '否',
        'myvs_7': '否',
        'myvs_8': '否',
        'myvs_9': 'y',
        'myvs_11': '否',
        'myvs_12': '否',
        'myvs_13': '否',
        'myvs_615': '否',
        'myvs_13a': '41',
        'myvs_13b': '4101',
        'myvs_13c': '科学大道100号',
        'myvs_24': '否',
        'myvs_26': '5',
        'memo22': '成功获取',
        'did': '2',
        'door': '',
        'day6': '',
        'men6': 'a',
        'sheng6': '41',
        'shi6': '',
        'fun18':'381',
        'fun3': '',
        'jingdu': '113.631419',
        'weidu': '34.753439',
        'ptopid': piopid,
        'sid': sid
    }
    yy=requests.post(url=url,headers=headers,data=data)
    yy.encoding = 'utf-8'
    yy = yy.text
    with open('./daka.html', 'w', encoding='UTF-8') as fp:
        fp.write(yy)
jksb()
jksb2()
