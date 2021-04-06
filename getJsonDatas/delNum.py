import os
import re
import pandas as pd

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
pd.set_option('display.max_colwidth', 100)

# 获取路径
rPath = os.getcwd()
dataPath = rPath + "\\dataSets"
fileList = os.listdir(dataPath)

filename = dataPath + "\\year.csv"
f = open(filename, 'r', encoding='utf-8-sig')
data = pd.read_csv(f, index_col=0)
f.close()

data["年份"] = data["年份"].apply(lambda x: re.sub('\(.*\)','',x))
print(data["年份"])

data.to_csv("newyear.csv", encoding='utf-8-sig')