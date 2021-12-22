# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:30:39 2020

@author: CEB
"""

import matplotlib.pyplot as plt

#数据准备
list_dead = [133,4512]
list_heal = [16340,63623]
list_nowconfirm = [362,0]
labels = ['非湖北地区','湖北地区']
font = {'family': 'SimHei', 'weight': 'normal', 'size': 20}

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(6,6))
#plt.title('湖北与非湖北地区治愈病例饼图',font)
#plt.pie(list_dead,autopct='%1.1f%%',labels=labels,shadow=False,startangle=110)
plt.pie(list_nowconfirm,autopct='%1.1f%%',labels=labels,explode=(0,0),shadow=False,startangle=90)
plt.axis('equal')
plt.legend(fontsize=15,ncol=1,bbox_to_anchor=(0.9, 0, 0.35, 1))
plt.savefig('img/湖北与非湖北地区重症病例饼图.jpg')
plt.show()