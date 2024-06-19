from asyncio import sleep
from datetime import time, datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver import Chrome, ActionChains, Keys
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
#登录
driver.get('https://rz.zjhu.edu.cn/cas/login?service=http://icspace.lib.zjhu.edu.cn')
#防止selenium被检测
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
    })
name = driver.find_element(by=By.ID, value='username')
name.send_keys('2021082320')    #输入学号
password = driver.find_element(by=By.ID, value='ppassword')
password.send_keys('@z12345678')    #输入密码
login = driver.find_element(by=By.ID, value='dl')
login.click()   #点击登录按钮
driver.implicitly_wait(1000)
el = driver.find_element(By.XPATH,value='/html/body/div/div[1]/div[3]/div[2]/div[1]/div/div[4]/div/div[2]') # 找到元素
ActionChains(driver).move_to_element(el).click().perform()
input_element = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[3]/div[2]/div[3]/div[2]/div/section/div/input')
input_element.clear()
input_element.send_keys("2024-06-01")
input_element.send_keys(Keys.ENTER)
driver.implicitly_wait(1000)
while True:
    strtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if (strtime == "2024-06-18 22:30:00"):
        el = driver.find_element(By.XPATH,
                                 value='/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[3]/div[1]/div/div[3]/span/button[1]')  # 找到元素
        ActionChains(driver).move_to_element(el).click().perform()
        break