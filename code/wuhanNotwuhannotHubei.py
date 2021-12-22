# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:00:12 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_excel(r'.\my_data\2020-06-20_wuhan_notWuhan_DayAdd_data.xlsx')
list_wuhan = list(data['wuhan'])
list_notWuhan = list(data['notWuhan'])
list_notHubei = list(data['notHubei'])
list_date = list(data['date'])

list_wuhan1 = []
list_notWuhan1 = []
list_notHubei1 = []
for i in range(len(list_wuhan)):
    if(list_wuhan[i]!=0):
        list_wuhan1.append(math.log(list_wuhan[i]))
    if(list_notWuhan[i]!=0):
        list_notWuhan1.append(math.log(list_notWuhan[i]))
    if(list_notHubei[i]!=0):
        list_notHubei1.append(math.log(list_notHubei[i]))
'''
#此方法用于更换日期格式,将日期转为正常格式输出
def changeDateFormat():
    list_date_x = []
    for i in range(len(list_date)):
        string_z = int(list_date[i])
        string_x = str(round((list_date[i]-string_z)*100))
        string_result = str(string_z)+'月'+string_x+"日"
        list_date_x.append(string_result)
    return list_date_x

#为降低日期显示出来的拥挤程度，选取每8个日期显示一次
list_date_x = changeDateFormat()
for i in range(len(list_date_x)):
    if (i%8==0 or i==len(list_date_x)-1):
        list_date_show.append(list_date_x[i])
'''

font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}
colors = ['red','green','blue']
alphas = [0.75,0.75,0.75]
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,7))
labels = ['Wuhan','the other city in Hubei','Outside Hubei Province']
data_show = (list_wuhan1,list_notWuhan1,list_notHubei1)
#plt.title('',font)
box = plt.boxplot(data_show,whis=0.45,widths=0.35,labels=labels,\
            vert=True,patch_artist=True,\
            medianprops = {'linestyle':'-','color':'black','lw':'3'})
for patch,color,alpha in zip(box['boxes'],colors,alphas):
    patch.set_facecolor(color)
    patch.set_alpha(alpha)

plt.tick_params(labelsize=15)
plt.ylabel('Numbers',font)
#plt.yticks(list(np.arange(-1.0, 10.5, 1.0)))
#fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
#plt.grid(axis='x',ls=':',c='black',alpha=0.7)
#plt.legend(prop=font)
#plt.savefig('img/新冠疫情发生以来我国时间-确诊病例曲线图.jpg')
plt.show()
