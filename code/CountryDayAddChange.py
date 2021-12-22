# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:44:56 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt

#变量定义
list_date_show = []

#读取文件获得对应列数据
data = pd.read_excel(r'.\my_data\2020-06-20_china_DayAdd_data.xlsx')
list_confirm = list(data['confirm'])
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
    if (i%8==0 or i==len(list_date_x)-1):
        list_date_show.append(list_date_x[i])

#特殊数据
confirm_max = max(list_confirm)
confirm_date_max = list_date_x[list_confirm.index(max(list_confirm))]


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,8))
#plt.title('时间-每日新增确诊病例曲线图')
plt.plot(list_date_x,list_confirm)
plt.annotate('February 12,'+'Newly confirmed cases reached the highest peak, newly added '+str(max(list_confirm))+' cases',\
             xy=(confirm_date_max,confirm_max),\
             xytext=(list_date_x[list_confirm.index(max(list_confirm))+2],confirm_max-1000),weight='regular',\
             color='r',fontsize=12,\
             arrowprops={'arrowstyle':'->',\
                         'connectionstyle':'arc3',\
                         'color':'r'})
plt.annotate('February 18,The turning point of the epidemic has arrived,\n and it is added on the same day'+str(list_confirm[list_date_x.index('2.18')])+'cases,\nSince then, the number of new cases every day \nhas shown a downward trend as a whole',\
             xy=('2.18',list_confirm[list_date_x.index('2.18')]),\
             xytext=(list_date_x[list_date_x.index('2.18')+1],list_confirm[list_date_x.index('2.18')]+2000),\
             weight='regular',\
             color='r',fontsize=12,\
             arrowprops={'arrowstyle':'->',\
                         'connectionstyle':'arc3',\
                         'color':'r'})
    
plt.xticks(list_date_show)
plt.yticks([i for i in range(0,16000,500)])
plt.xlabel('Date')
plt.ylabel('Number of newly confirmed cases per day')
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.grid(axis='x',ls=':',c='black',alpha=0.7)
fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#plt.savefig('img/每日新增确诊病例曲线图.jpg')
plt.show()
