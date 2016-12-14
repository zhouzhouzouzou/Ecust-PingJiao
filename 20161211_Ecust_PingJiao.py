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
        normal = re.findall('href=\"pg\.php(.*?)\"',login.text)
        yypg = re.findall('href=\"yypg\.php(.*?)\"',login.text)
        typg = re.findall('href=\"typg\.php(.*?)\"',login.text)
        bdspg = re.findall('href=\"bdspg\.php(.*?)\"',login.text)
        normalList = []
        yypgList = []
        typgList = []
        bdspgList = []
        for i in range(0, len(normal)):
            normalList.append('http://pjb.ecust.edu.cn/pingce/pg.php' + normal[i])
        for i in range(0, len(yypg)):
            yypgList.append('http://pjb.ecust.edu.cn/pingce/yypg.php' + yypg[i])
        for i in range(0, len(typg)):
            typgList.append('http://pjb.ecust.edu.cn/pingce/typg.php' + typg[i])
        for i in range(0, len(bdspg)):
            bdspgList.append('http://pjb.ecust.edu.cn/pingce/bdspg.php' + bdspg[i])
        cookies = r.cookies
        br.set_cookiejar(cookies)
        for i in range(0,len(normalList)):
            pj_normal(normalList[i])
        for i in range(0,len(yypgList)):
            pj_normal(yypgList[i])
        for i in range(0,len(typgList)):
            pj_normal(typgList[i])
        for i in range(0,len(bdspgList)):
            pj_normal(bdspgList[i])


    except Exception , e:
        print Exception,':',e
        return 'Found a bug. Please contact the author.'

def pj_normal(url):
    r = br.open(url)
    br.select_form(name='Form1')
    html = r.read().decode('gbk').encode('utf-8')
    for i in range(1,20):
        values = re.findall(r'name="yq'+str(i)+'"\svalue="(.*?)"', html, re.S)
        if len(values) != 0:
            br.form['yq'+str(i)] = [values[0]]
    br.submit()

main('10150982','125018')