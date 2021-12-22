# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:34:31 2020

@author: CEB
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

list_date_show = []

data = pd.read_excel(r'.\my_data\2020-06-20_china_history_data.xlsx')
list_confirm = list(data['confirm'])
list_date = list(data['date'])
font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}

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

#构建函数模型，准备步长，运算特定条件下，传染病模型的增长速率
list_x = list(np.arange(0, 44, 0.01))
list_y = []
for i in range(len(list_x)):
    list_y.append(((3**(list_x[i]/4))-1)/2)



plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,7))
plt.title('Confirmed cases in China-ideal infectious disease model',font)
plt.plot(list_date_x,list_confirm,label='Confirmed cases in China')
plt.plot(list_x,list_y,label='ideal infectious disease model')
plt.xticks(list_date_show)
plt.yticks([i for i in range(0,90000,4000)])
plt.xlabel('Date',font)
plt.ylabel('numbers',font)
fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.grid(axis='x',ls=':',c='black',alpha=0.7)
plt.legend(prop=font)
#plt.savefig('img/我国确诊病例-理想传染病模型曲线图.jpg')
plt.show()
