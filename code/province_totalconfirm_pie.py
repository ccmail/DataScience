# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:54:51 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r'F:\(重要！)学习资料\python数据可视化\期末论文源代码\my_data\2020-06-20_china_province_data.xlsx')
list_province = list(data['province'])
list_total_nowconfirm = list(data['total_nowconfirm'])
explodes = []
for i in range(len(list_total_nowconfirm)):
    if(list_total_nowconfirm[i]==max(list_total_nowconfirm)):
        explodes.append(0.05)
    else:
        explodes.append(0)

font = {'family': 'SimHei', 'weight': 'normal', 'size': 20}

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(10,10))
#plt.title('各省份现存确诊病例饼图',font)
wedges, texts = plt.pie(list_total_nowconfirm,explode=tuple(explodes),\
        shadow=False,startangle=90)
plt.axis('equal')
plt.legend(wedges,
           list_province,
           fontsize=15,
           title="省份",
           loc="lower center",
           ncol=2,
           bbox_to_anchor=(0.99, 0.15, 0.35, 1))
plt.savefig('img/各省份确诊病例数饼图.jpg')
plt.show()
