# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:20:54 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#该包用于对数据集的数据预处理
import sklearn.preprocessing as spre

list_date_show = []

data = pd.read_excel(r'.\my_data\2020-06-20_china_DayAdd_data.xlsx')
data1 = pd.read_excel(r'.\my_data\2020-06-20_china_history_data.xlsx')
index_number = data1[(data1['date']==1.2)].index.tolist()[0]

list_date = list(data['date'])
list_dead = list(data['dead'])
list_heal = list(data['heal'])
list_nowSevere =list(data1['nowSevere'][index_number:])
list_deadRate = list(data1['deadRate'][index_number:])
list_healRate = list(data1['healRate'][index_number:])
dict_data = {'dead':list_dead,'heal':list_heal,'nowSevere':list_nowSevere,\
             'deadRate':list_deadRate,'healRate':list_healRate}
data_new = pd.DataFrame(dict_data)
#对数据进行标准化
data_new1 = spre.StandardScaler().fit_transform(data_new)
data_new1 = pd.DataFrame(data_new1)
#此方法用于更换日期格式,将日期转为正常格式输出
def changeDateFormat():
    list_date_x = []
    for i in range(len(list_date)):
        string_z = int(list_date[i])
        string_x = str(round((list_date[i]-string_z)*100))
        string_result = str(string_z)+'.'+string_x
        list_date_x.append(string_result)
    return list_date_x

#为降低日期显示出来的拥挤程度，选取每8个日期显示一次
list_date_x = changeDateFormat()
for i in range(len(list_date_x)):
    if (i%8==0 or i==len(list_date_x)-1):
        list_date_show.append(list_date_x[i])

font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,7))

plt.title('Mortality-Cure Rate-Number of Severe Cases Curve',font)
plt.plot(list_date_x,list(data_new1[3]),label='Daily mortality',color='r',alpha=0.5)
plt.plot(list_date_x,list(data_new1[4]),label='Daily cure rate',color='b',alpha=0.7)
plt.plot(list_date_x,list(data_new1[2]),label='Existing severe cases',color='green')
plt.xlabel('Date',font)
plt.ylabel('Rate %',font)

plt.xticks(list_date_show)
plt.yticks(list(np.arange(-1.0, 6.0, 0.5)))
fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.grid(axis='x',ls=':',c='black',alpha=0.7)
plt.legend(prop=font)
#plt.savefig('img/新冠疫情发生以来我国时间-确诊病例曲线图.jpg')
plt.show()