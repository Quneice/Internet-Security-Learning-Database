import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def exp_check(url):
    try:
        path = "/ruc/Software/SoftUpload.aspx"
        rsp = requests.get(url= url + path, headers=headers,verify=False)
        pass
    except:
        return 3

def exp_upload(url,data,shellName):
    pass