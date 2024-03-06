import pandas as pd
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import EdgeOptions
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 列名
columns = ["名称", "类别", "申报单位", "保护单位"]
# 创建空的 DataFrame
df = pd.DataFrame(columns=columns)

s = Service(executable_path=r'D:/msedgedriver.exe')
browser = webdriver.Edge(service=s)
name_list = []
type_list = []
apply_list = []
protect_list = []
number_list = []
url_browser = "https://www.ihchina.cn/project.html#target1"
browser.get(url_browser)
time.sleep(3)

while True:
    try:
        time.sleep(5)
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "next")))
        if button.is_displayed():
            for i in range(2, 12):
                name = browser.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[5]/table/tbody/tr[{}]/td[4]/a".format(i)).text
                types=browser.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div[5]/table/tbody/tr[{}]/td[7]".format(i)).text
                apply = browser.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[5]/table/tbody/tr[{}]/td[8]".format(i)).text
                protect = browser.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[5]/table/tbody/tr[{}]/td[9]".format(i)).text
                number = browser.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div[5]/table/tbody/tr[{}]/td[1]".format(i)).text
                name_list.append(name)
                type_list.append(types)
                apply_list.append(apply)
                protect_list.append(protect)
                number_list.append(number)
            time.sleep(5)
            button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        break

df["名称"] = name_list
df["类别"] = type_list
df["申报单位"] = apply_list
df["保护单位"] = protect_list
df.to_excel("./非遗名录.xlsx")