import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def save2csv(dic_list):
    pd.DataFrame(dic_list).to_csv('report_info4.csv', encoding='utf-8-sig')


# 创建浏览器对象
browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')

# 向浏览器发送请求
browser.get("https://feed.watcherlab.com/index/apt")

# 等待3秒
time.sleep(3)

apt_buttun = browser.find_element_by_xpath("//div[@class=' ant-tabs-tab']")
apt_buttun.click()
# browser.execute_script("arguments[0].click();", apt_buttun)
id = 1

dic_list = []
for i in range(150, 187):
    # 进入页面，定位信息
    # time.sleep(3)
    apt_btn = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/span[%d]" % i)
    browser.execute_script("arguments[0].click();", apt_btn)
    time.sleep(1)
    apt_name = browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/span[%d]" % i).text
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
        #                                  //*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div
        p_time = rl.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[%d]/div[2]/div/div[1]/div" % c).text
        #                                     //*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div
        p_company = rl.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[%d]/div[2]/div/div[2]/div" % c).text
        #                                       //*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[4]/div
        attack_tips = rl.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[%d]/div[2]/div/div[4]/div" % c).text
        #                                   //*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[7]
        #                                   //*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[7]/span
        try:
            expand_btn = rl.find_element_by_xpath("//a[@class='ant-typography-expand']")
            if expand_btn:
                browser.execute_script("arguments[0].click();", expand_btn)
        except:
            pass
        details = rl.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[%d]/div[2]/div/div[7]" % c).text

        # try:
        #     attack_tips_list = []
        #     # num = 1
        #     for one_tip in attack_tips:
        #         print(one_tip.text)
        #         #                             //*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[4]/div/span[2]
        #         x = one_tip.find_element_by_xpath("span").text
        #         print(x)
        #         # num += 1
        #         attack_tips_list.append(x)
        # except:
        #     pass


        c += 1

        dic = {
            '报告标题': l.text,
            'APT组织': apt_name,
            '披露时间': p_time,
            '披露机构': p_company,
            '攻击方法': attack_tips,
            '报告摘要': details
        }
        print(dic)
        dic_list.append(dic)
    print("+++++++++++++++++++")


save2csv(dic_list)