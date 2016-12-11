#coding=utf-8
import mechanize
import requests
import re

def main(sno=None,password=None):
    global br
    #browser
    br = mechanize.Browser()
    r = requests.Session()
    if sno is None or password is None:
        print "你还没有输入账号或密码"
    #options
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    try:
        loginUrl = 'http://pjb.ecust.edu.cn/pingce/login.php'
        login = r.post(url=loginUrl,data={'action':'login','sno':sno,'password':password})
        spider = re.findall('href="pg\.php+(.*?)"',login.text,re.S)
        length = len(spider)
        spiderList = []
        for i in range(0, length - 1):
            spiderList.append('http://pjb.ecust.edu.cn/pingce/pg.php' + spider[i])
        pingCe = []
        for i in range(0, length - 1):
            pingCe.append(r.get(url=spiderList[i]).text)
        print pingCe

        cookies = r.cookies
        br.set_cookiejar(cookies)

    except Exception , e:
        print Exception,':',e

main('10150982','125018')