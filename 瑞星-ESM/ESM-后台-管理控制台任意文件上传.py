

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Length': '19',

}

def changeHeaderCookies(cookie:dict):
    cookies = cookie
    headers.update(cookies)
    
     

def exp_check(url):
    requests.get()
