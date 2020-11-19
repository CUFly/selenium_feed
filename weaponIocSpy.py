import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def save2file(dic_list):
    pd.DataFrame(dic_list).to_excel('WeaponIocs.xlsx')

# 创建浏览器对象
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')

# 向浏览器发送请求
browser.get("https://feed.watcherlab.com/index/apt")

# 等待3秒
time.sleep(3)

apt_buttun = browser.find_element_by_xpath("//div[@class='ant-tabs-nav ant-tabs-nav-animated']/div/div[6]")
apt_buttun.click()
# browser.execute_script("arguments[0].click();", apt_buttun)
id = 1

title_list = []
filename_list = []
dic_list = []
for i in range(1, 221):   # 1-220
    # 进入页面，定位信息
    # time.sleep(3)
    weapon_btn = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/div[3]/div[6]/span[%d]" % i)
    browser.execute_script("arguments[0].click();", weapon_btn)
    time.sleep(1)
    weapon_name = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/div[3]/div[6]/span[%d]" % i).text
    # time.sleep(3)
    # list = browser.find_elements_by_xpath("//div[@class='ant-collapse-item']")

    list = browser.find_elements_by_xpath("//div[@class='ant-typography ant-typography-ellipsis ant-typography-ellipsis-single-line']")
    # report_list = browser.find_elements_by_xpath("//div[@class='ant-collapse ant-collapse-icon-position-left']")
    flag = True
    c = 1  # 用来定位
    for l in list:
        if flag:  # 首次进入，关闭所有标签，以统一动作
            browser.execute_script("arguments[0].click();", l)
            flag = False
        # print(l.text)
        browser.execute_script("arguments[0].click();", l)
        time.sleep(3)
        content = browser.find_element_by_xpath("//div[@class='ant-collapse-content-box']")
        rl = content
        r_title = rl.find_element_by_xpath("//div[@class='ant-typography ant-typography-ellipsis ant-typography-ellipsis-single-line']").text
        try:
            down = rl.find_element_by_xpath("//div[@class='antd-pro-pages-home-components-apt-list-flex']/a[3]")
            down_title = down.get_attribute('download')
            try:
                down_btn = rl.find_element_by_xpath("//button[@class='ant-btn antd-pro-pages-home-components-apt-list-btn3 ant-btn-primary ant-btn-sm']")
                if down_btn:
                    browser.execute_script("arguments[0].click();", down_btn)
                    title_list.append(l.text)
                    filename_list.append(down_title)
                    dic = {
                        'title': l.text,
                        'name': down_title,
                    }
                    print(dic)
                    dic_list.append(dic)
            except:
                pass
        except:
            pass

    print("+++++++++++++++++++")


save2file(dic_list)
print(title_list)
print(filename_list)