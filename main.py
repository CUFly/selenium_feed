import time
import pandas as pd
from selenium import webdriver

# def save2csv(dic):
#     with open('test.csv', 'a', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f, )
#         for key,value in dic.items():
#             writer.writerow([key, value])

def save2csv(dic_list):
    """
    写入csv
    :param dic_list:
    :return:
    """
    pd.DataFrame(dic_list).to_csv('apt_info2.csv', encoding='utf-8-sig')

# 创建浏览器对象
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')

# 向浏览器发送请求
browser.get("https://feed.watcherlab.com/index/apt")

# 等待3秒
time.sleep(3)

# 点开“按APT”选项卡
apt_buttun = browser.find_element_by_xpath("//div[@class='ant-tabs-tab']")
apt_buttun.click()

dic_list = []
for i in range(1, 187):
    # 进入页面，定位信息
    apt_buttun = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/span[%d]" % i).click()
    # time.sleep(3)
    apt_name = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/span[%d]" % i).text
    print(apt_name)
    list = browser.find_elements_by_xpath("//div[@class='antd-pro-components-k-v-layout-index-right undefined']")
    print(list)
    s_belong = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div").text
    print(s_belong)
    o_name = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div").text
    print(o_name)
    o_n_list = []
    for on in o_name:
        o_n_list.append(on)
    text_list = []
    for l in list:
        text_list.append(l.text)
    dic = {
        "APT组织": apt_name,
        "可疑归属": s_belong,
        "组织别名": o_name,
        "攻击手法": text_list[3],
        "攻击国家/地区": text_list[4],
        "攻击行业": text_list[5],
        "恶意软件": text_list[6],
        "攻击工具": text_list[7],
        "事件介绍": text_list[8]
    }
    print(dic)
    dic_list.append(dic)

# save2csv(dic_list)
