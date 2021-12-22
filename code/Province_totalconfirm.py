# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:27:46 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel(r'F:\(重要！)学习资料\python数据可视化\期末论文源代码\my_data\2020-06-20_china_province_data.xlsx')
list_province = list(data['province'])
list_total_confirm = list(data['total_confirm'])

font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(20,10))
#plt.title('各省份确诊病例总数柱状图',font)
plt.bar(list_province,list_total_confirm,facecolor='blue',alpha=0.7)
for i in range(len(list_province)):
    plt.text(list_province[i],list_total_confirm[i],list_total_confirm[i],ha='center',va='bottom')
plt.xticks(list_province)
plt.yticks([i for i in range(0,70000,2000)])
plt.xlabel('城市',font)
plt.ylabel('确诊病例数',font)
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.savefig('img/各省份确诊病例总数柱状图.jpg')
plt.show()