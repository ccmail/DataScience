# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:00:49 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

list_date_show = []

data = pd.read_excel(r'.\my_data\2020-06-20_hubei_notHubei_DayAdd_data.xlsx')
list_hubei = list(data['hubei'])
list_nothubei = list(data['notHubei'])
list_date = list(data['date'])
list_hubei1 = []
list_nothubei1 = []
for i in range(len(list_hubei)):
    if(list_hubei[i]!=0):
        list_hubei1.append(math.log(list_hubei[i]))
    if(list_nothubei[i]!=0):
        list_nothubei1.append(math.log(list_nothubei[i]))

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
colors = ['blue','blue']
alphas = [0.75,0.75]
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(8,7))
labels = ['Hubei Province','Non-Hubei Province']
data_show = (list_hubei1,list_nothubei1)
#plt.title('湖北-非湖北地区每日新增确诊病例数箱图',font)
box = plt.boxplot(data_show,whis=0.55,widths=0.3,labels=labels,\
            vert=True,patch_artist=True,\
            medianprops = {'linestyle':'-','color':'black','lw':'3'})
for patch,color,alpha in zip(box['boxes'],colors,alphas):
    patch.set_facecolor(color)
    patch.set_alpha(alpha)

plt.tick_params(labelsize=15)
plt.ylabel('Numbers',font)
plt.yticks(list(np.arange(-1.0, 10.5, 1.0)))
#fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
#plt.grid(axis='x',ls=':',c='black',alpha=0.7)
#plt.legend(prop=font)
#plt.savefig('img/湖北-非湖北地区每日新增确诊病例数箱图.jpg')
plt.show()
