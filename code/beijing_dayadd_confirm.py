# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:28:05 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt

#变量定义
list_date_show = []

#读取文件获得对应列数据
data = pd.read_excel(r'..\data\2020-06-11-07-04_beijing_DayAdd_data.xlsx')
list_confirm = list(data['today_confirm'])
list_date = list(data['date'])

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
    if (i%1==0 or i==len(list_date_x)-1):
        list_date_show.append(list_date_x[i])

#特殊数据
confirm_max = max(list_confirm)
confirm_date_max = list_date_x[list_confirm.index(max(list_confirm))]


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,8))
#plt.title('时间-每日新增确诊病例曲线图')
plt.plot(list_date_x,list_confirm)
plt.xticks(list_date_show)
plt.yticks([i for i in range(0,40,5)])
plt.xlabel('Date')
plt.ylabel('Number of newly confirmed cases')
fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.grid(axis='x',ls=':',c='black',alpha=0.7)
#plt.savefig('img/北京新发地每日新增确诊病例曲线图.jpg')
plt.show()
