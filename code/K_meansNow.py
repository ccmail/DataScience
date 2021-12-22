# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:24:28 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt
#导入K-means
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabaz_score

#读取数据
data = pd.read_excel(r'F:\(重要！)学习资料\python数据可视化\期末论文源代码\my_data\2020-06-20_china_city_data.xlsx')
#数据预处理，清洗掉无用的维度，留下与分析相关的维度与数据
list_total_nowconfirm = list(data['total_nowconfirm'])
list_today_confirm = list(data['today_confirm'])
dict_data = {'total_nowconfirm':list_total_nowconfirm,'today_confirm':list_today_confirm}
data_result = pd.DataFrame(dict_data) 

#确定最优K值
#导入K-means
#from sklearn.cluster import KMeans
#from sklearn.metrics import calinski_harabaz_score
def sureBestK():
    list_a = []
    for i in range(2,6):
        km = KMeans(n_clusters = i).fit(data_result)
        a = calinski_harabaz_score(data_result,km.labels_)#使用兰德系数作为判定指标
        #print('i=',i,'a=',a)
        list_a.append(a)
    return list_a.index(max(list_a))+2

#from sklearn.cluster import KMeans
#使用K-means聚类算法训练数据集
km = KMeans(n_clusters=sureBestK()).fit_predict(data_result)
list_km = list(km)
#可视化部分
colors = ['blue','red','orange','yellow','black']
font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10,6))
#plt.title('对当前疫情状况进行聚类分析后结果散点图',font)
plt.scatter(list_total_nowconfirm, list_today_confirm,c=km,s=60)
plt.xlabel('现有确诊病例数',font)
plt.ylabel('当日新增确诊病例数',font)
plt.xticks([i for i in range(0,150,5)])
plt.yticks([i for i in range(0,15,1)])
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.5)
plt.grid(axis='x',ls=':',c='black',alpha=0.5)
#plt.savefig('img/聚类分析结果图.jpg')
plt.show()
