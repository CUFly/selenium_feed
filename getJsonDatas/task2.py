import os
import json
import pandas as pd

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
pd.set_option('display.max_colwidth', 100)

# 获取路径
rPath = os.getcwd()
dataPath = rPath + "\\dataSets"
# fileList = os.listdir(dataPath)
fr = open("apt.json", 'r', encoding='utf-8')
aptDict = json.load(fr)
fr.close()

# 对newapt.csv进行归并处理
with open("dataSets/newapt.csv", 'r', encoding='utf-8-sig') as f1:
    data1 = pd.read_csv(f1, index_col=0)
data1 = data1.fillna("")
m1, n1 = data1.shape
flag_apt = "Ajax Security Team "
curr_apt = ""    # 当前组织名
eventList = []
eventDict = {}
for i in range(m1):
    curr_apt = data1.iloc[i][0]
    if curr_apt != flag_apt:
        # 如果当前的apt与上一个组织不同，则将eventList添加到aptDict中
        aptDict[flag_apt]["Events"] = eventList
        eventList = []
        flag_apt = curr_apt
    eventDict["报告标题"] = data1.iloc[i][1]
    eventDict["披露时间"] = data1.iloc[i][2]
    eventDict["披露机构"] = data1.iloc[i][3]
    eventDict["攻击方法"] = data1.iloc[i][4]
    eventDict["报告摘要"] = data1.iloc[i][6]
    eventList.append(eventDict)
    eventDict = {}

with open("res.json", "w", encoding='utf-8') as f:
    json.dump(aptDict, f, ensure_ascii=False)


