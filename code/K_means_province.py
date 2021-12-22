# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:37:12 2020

@author: CEB
"""

import pandas as pd
#导入K-means
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabaz_score
#导入pyecharts绘制全国疫情图
from pyecharts.charts import Map
from pyecharts import options as opts
#读取数据
data = pd.read_excel(r'F:\(重要！)学习资料\数据挖掘\期末论文\data\2020-06-28_china_province_data.xlsx')
#数据预处理，清洗掉无用的维度，留下与分析相关的维度与数据
list_total_nowconfirm = list(data['total_nowconfirm'])
list_today_confirm = list(data['today_confirm'])
list_province = list(data['province'])
dict_data = {'total_nowconfirm':list_total_nowconfirm,'today_confirm':list_today_confirm}
data_result = pd.DataFrame(dict_data) 

#确定最优K值
def sureBestK():
    list_a = []
    for i in range(2,6):
        km = KMeans(n_clusters = i).fit(data_result)
        a = calinski_harabaz_score(data_result,km.labels_)
        #print('i=',i,'a=',a)
        list_a.append(a)
    return list_a.index(max(list_a))+2

km = KMeans(n_clusters=sureBestK()).fit_predict(data_result)
list_km = list(km)
province_distribution = dict((name,value) for name,value in zip(list_province,list_km))

# maptype='china' 只显示全国直辖市和省级
map1 = Map()
map1.set_global_opts(
    title_opts=opts.TitleOpts(title="20200628各省份疫情数据聚类结果地图"),
    visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True,
                                      pieces=[
                                        {"value":4, "label": "第五类", "color": "#8A0808"},
                                        {"value":3, "label": "第四类", "color": "#FFA500"},
                                        {"value":2, "label": "第三类", "color": "#7FFF00"},
                                        {"value":1, "label": "第二类", "color": "#FFFF00"},
                                        {"value":0, "label": "第一类", "color": "#FFFFFF"},
                                        ], )  #最大数据范围，分段
    )
map1.add("20200628各省份疫情数据聚类结果地图", data_pair=list(province_distribution.items()),\
         maptype="china", is_roam=True)
map1.render('20200628各省份疫情数据聚类结果地图.html')
