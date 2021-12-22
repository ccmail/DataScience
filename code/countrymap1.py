# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:47:09 2020

@author: CEB
"""

from pyecharts.charts import Map
from pyecharts import options as opts
import pandas as pd

data = pd.read_excel(r'.\my_data\2020-06-28_china_province_data.xlsx')
list_province = list(data['province'])
list_total_nowconfirm = list(data['total_nowconfirm'])
province_distribution = dict((name,value) for name,value in zip(list_province,list_total_nowconfirm))

# maptype='china' 只显示全国直辖市和省级
map = Map()
map.set_global_opts(
    title_opts=opts.TitleOpts(title="Map of the clustering results of epidemic data in various provinces in 20200628"),
    visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True,
                                      pieces=[
                                        #{"max": 5000, "min": 1001, "label": "第六类", "color": "#8A0808"},
                                        {"max": 1000, "min": 100, "label": "第五类", "color": "#8A0808"},
                                        {"max": 100, "min": 16, "label": "第四类", "color": "#FFA500"},
                                        {"max": 15, "min": 6, "label": "第三类", "color": "	#7FFF00"},
                                        {"max": 5, "min": 1, "label": "第二类", "color": "#FFFF00"},
                                        {"max": 0, "min": 0, "label": "第一类", "color": "#FFFFFF"},
                                        ], )  #最大数据范围，分段
    )
map.add("Map of the clustering results of epidemic data in various provinces in 20200628", data_pair=list(province_distribution.items()), maptype="china", is_roam=True)
map.render('img/20200620中国疫情地图.html')