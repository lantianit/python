import json
import threading
from datetime import datetime
from time import sleep
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ActionChains, Keys
from selenium.webdriver.common.by import By

def auto_reserve() :
    while True :
        if (datetime.now().strftime('%Y-%m-%d %H:%M:%S') == "2024-05-13 22:29:57"):
            while True :
                q = requests.post("http://icspace.lib.zjhu.edu.cn/ic-web/reserve", data=json.dumps(payload),
                                         headers=request_header)
                print(q.json())

option = Options()
option.add_experimental_option("detach", True)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
# 登录
driver.get('https://rz.zjhu.edu.cn/cas/login?service=http://icspace.lib.zjhu.edu.cn')
# 防止selenium被检测
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
name = driver.find_element(by=By.ID, value='username')
name.send_keys('2021082320')  # 输入学号
password = driver.find_element(by=By.ID, value='ppassword')
password.send_keys('@z12345678')  # 输入密码
login = driver.find_element(by=By.ID, value='dl')
login.click()  # 点击登录按钮
sleep(1)
cookie = driver.get_cookies()
cookie = cookie[0]
cookie = cookie.get('value')
request_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "icspace.lib.zjhu.edu.cn",
    "lan": "1",
    "Referer": "http://icspace.lib.zjhu.edu.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"
}
request_header["Cookie"] = "ic-cookie=" + cookie
cookie = "ic-cookie=" + cookie
print(request_header)
response = requests.get("http://icspace.lib.zjhu.edu.cn/ic-web/auth/userInfo", headers=request_header)
token = (response.json()).get("data").get("token")
request_header = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Length": "216",
    "Content-Type": "application/json;charset=UTF-8",
    "Connection": "keep-alive",
    "Host": "icspace.lib.zjhu.edu.cn",
    "lan": "1",
    "Origin": "http://icspace.lib.zjhu.edu.cn",
    "Referer": "http://icspace.lib.zjhu.edu.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"
}
request_header["Cookie"] = cookie
request_header["token"] = token
payload = {"sysKind": 8, "appAccNo": 74206, "memberKind": 1, "resvMember": [74206],
           "resvBeginTime": "2024-05-15 15:00:00",
           "resvEndTime": "2024-05-15 22:00:00",
           "testName": "", "captcha": "", "resvProperty": 0, "resvDev": [100458082], "memo": ""
           }
t1 = threading.Thread(target=auto_reserve,name = "MyThread1")
t1.start()
t1.join()
