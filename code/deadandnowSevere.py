# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:40:19 2020

@author: CEB
"""
#导入包
import pandas as pd #pandas库用于读取文件并把数据集转为DataFrame类型数据
import matplotlib.pyplot as plt #进行数据可视化库
import numpy as np #numpy库进行部分数据处理
#该包用于对数据集的数据预处理
import sklearn.preprocessing as spre

#定义全局变量，用于保存要显示的日期
list_date_show = []

data = pd.read_excel(r'F:\(重要！)学习资料\python数据可视化\期末论文源代码\my_data\2020-06-20_china_history_data.xlsx')
data_new = data[['deadRate','dead','heal','healRate','nowSevere']]

#2数据预处理
#2.1对数据进行标准化
data_new1 = spre.StandardScaler().fit_transform(data_new)
data_new1 = pd.DataFrame(data_new1)
list_date = list(data['date'])
#list_dead = data_new1[1]
list_deadRate = data_new1[0]
list_healRate = data_new1[3]
list_nowSevere = data_new1[4]

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

#3数据可视化
#定义字体样式
font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}
#设置字体中文显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig = plt.figure(figsize=(10,7))
plt.title('死亡病例-重症病例曲线关系图',font)
plt.plot(list_date_x,list_healRate,label='治愈率')
plt.plot(list_date_x,list_deadRate,label='死亡率')
plt.plot(list_date_x,list_nowSevere,label='现有重症病例')
plt.xticks(list_date_show)
plt.yticks(list(np.arange(-3.0, 3.5, 0.5)))
plt.xlabel('日期',font)
plt.ylabel('数据',font)
fig.autofmt_xdate() # 让x轴标签斜着打印避免拥挤
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.grid(axis='x',ls=':',c='black',alpha=0.7)
plt.legend(prop=font)
#plt.savefig('img/新冠疫情发生以来我国时间-确诊病例曲线图.jpg')
plt.show()
