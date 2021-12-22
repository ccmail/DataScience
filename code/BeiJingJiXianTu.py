# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:39:05 2020

@author: CEB
"""

import numpy as np
import matplotlib.pyplot as plt

font = {'family': 'SimHei', 'weight': 'normal', 'size': 25}
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,7))
labels = np.array(['total_nowconfirm',\
                   'total_suspect','total_dead','total_heal',\
                   'today_confirm']) # 标签
dataLenth = 5  # 数据长度
data_radar = np.array([206,0,9,584,22]) # 数据
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)  # 分割圆周长
data_radar = np.concatenate((data_radar, [data_radar[0]]))  # 闭合
angles = np.concatenate((angles, [angles[0]]))  # 闭合
plt.polar(angles, data_radar, 'bo-', linewidth=1)  # 做极坐标系
plt.thetagrids(angles * 180/np.pi, labels,fontsize=20)  # 做标签
plt.fill(angles, data_radar, facecolor='r', alpha=0.25)# 填充
plt.ylim(0, 500)
#plt.title('2020-06-20北京市疫情各方面数据雷达图',font)
#plt.savefig('img/2020-06-20北京市疫情各方面数据雷达图.jpg')
plt.show()
