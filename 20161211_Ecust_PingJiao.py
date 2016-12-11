#coding=utf-8
import mechanize
import requests

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
        listUrl = 'http://pjb.ecust.eud.cn/pingce/list.php'
        login = r.post(url=loginUrl,data={'action':'login','sno':sno,'password':password})
        list = r.get(url=listUrl)
        cookies = r.cookies
        br.set_cookiejar(cookies)
        print login.text
    except Exception , e:
        print Exception,':',e

main('10150982','125018')