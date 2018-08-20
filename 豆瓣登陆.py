import urllib
import requests
from bs4 import BeautifulSoup

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
session = requests.Session()

response1 = session.get('https://accounts.douban.com/login',headers = headers).text
bsObj = BeautifulSoup(response1,'lxml')
captcha_img = bsObj.find('img',{'id':'captcha_image'})
if captcha_img:
    captcha_img = bsObj.find('img',{'id':'captcha_image'})['src']
    path = '.\captcha.png'
    urllib.request.urlretrieve(captcha_img,path)
    captchaid = captcha_img.split('=')[1].split("&")[0]
    captcha = input("输入验证码：》》")
    data = [
        ('soure','None'),
        ('redir','https://www.douban.com/'),
        ('from_email', '331251614@qq.com'),
        ('form_password', 'ydzly1991911'),
        ('captcha-solution', captcha),
        ('captcha-id', captchaid),
        ('login', '\u767B\u5F55'),
         ]

    session.post("https://accounts.douban.com/login",headers = headers ,data = data)
    params = (
        ('start','220'),
        ('limit', '20'),
        ('sort', 'new_score'),
        ('status', 'P'),
        ('percent_type', ''),
    )

    r2 = session.get("https://movie.douban.com/subject/27041389/comments?",headers = headers,data= data)
else:
    data = [
        ('soure','None'),
        ('redir','https://www.douban.com/'),
        ('from_email', '331251614@qq.com'),
        ('form_password', 'ydzly1991911'),
        ('login', '\u767B\u5F55'),
         ]
    session.post("https://www.douban.com/accounts/login?source=main", headers=headers, data=data)
    params = (
        ('start', '220'),
        ('limit', '20'),
        ('sort', 'new_score'),
        ('status', 'P'),
        ('percent_type', ''),
    )
    r2 = session.get("https://movie.douban.com/subject/27041389/comments?", headers=headers, data=data)


print(r2.text)

