# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:08:12 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

list_date_show = []

data = pd.read_excel(r'.\my_data\2020-06-20_hubei_history_data.xlsx')
data1 = pd.read_excel(r'.\my_data\2020-06-20_notHubei_history_data.xlsx')

list_date = list(data['date'])
list_hubei_deadRate = list(data['deadRate'])
list_hubei_healRate = list(data['healRate'])
list_nothubei_deadRate = list(data1['deadRate'])


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
fig = plt.figure(figsize=(11,7))
font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,7))

#plt.title('湖北与非湖北地区死亡率对比曲线图',font)
plt.plot(list_date_x,list_hubei_deadRate,label='Hubei mortality rate',color='r',alpha=0.5)
plt.plot(list_date_x,list_nothubei_deadRate,label='Non-Hubei mortality rate',color='b',alpha=0.7)
plt.xlabel('Date',font)
plt.ylabel('mortality rate %',font)
plt.xticks(list_date_show)
plt.yticks(list(np.arange(-1.0, 7.5, 0.5)))
fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.grid(axis='x',ls=':',c='black',alpha=0.7)
plt.legend(loc="lower right",prop=font)
#plt.savefig('img/湖北与非湖北地区死亡率对比曲线图.jpg')
plt.show()

