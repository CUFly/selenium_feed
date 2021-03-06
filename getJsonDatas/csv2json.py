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
fileList = os.listdir(dataPath)

byApt = dataPath + "\\ByAPT.csv"
f = open(byApt, 'r', encoding='utf-8-sig')
data = pd.read_csv(f)
f.close()
data = data.fillna("")
# apt字典
aptDict = {}
r, c = data.shape     # (行数，列数)
for i in range(r):    # 按行遍历
    aptDict[data.iloc[i][0]] = {
        "Country": data.iloc[i][1],
        "Nickname": data.iloc[i][2],
    }
# res = json.dumps(aptDict)
with open("apt.json", "w", encoding='utf-8') as f:
    json.dump(aptDict, f)










