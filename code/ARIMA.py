# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:38:48 2020

@author: CEB
"""

import pandas as pd
import matplotlib.pyplot as plt
#导入ARIMA库
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm

font = {'family': 'SimHei', 'weight': 'normal', 'size': 15}
data = pd.read_excel(r'..\data\2020-06-11-07-04_beijing_DayAdd_data.xlsx')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#对数据进行差分并可视化

data['diff_1'] = data['today_confirm'].diff(1)
data['diff_2'] = data['diff_1'].diff(2)
'''
fig = plt.figure(figsize=(20,6))
ax1 = fig.add_subplot(131)
ax1.plot(data['today_confirm'])
ax2 = fig.add_subplot(132)
ax2.plot(data['diff_1'])
ax3 = fig.add_subplot(133)
ax3.plot(data['diff_2'])
'''
'''
#绘制自相关函数ACF和非自相关函数图PACF
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(data['today_confirm'], lags=20,ax=ax1)
ax1.xaxis.set_ticks_position('bottom')
fig.tight_layout()
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(data['today_confirm'], lags=20, ax=ax2)
ax2.xaxis.set_ticks_position('bottom')
fig.tight_layout()
'''


model = sm.tsa.ARIMA(data['today_confirm'], order=(1, 2, 1))
results = model.fit()
residuals = pd.DataFrame(results.resid)
print(results.summary())
print(residuals.describe())
predict_sunspots = results.predict(dynamic=False)
list_temp = list(predict_sunspots)
list_predict_sunspots = []
for i in range(len(list_temp)):
    if(list_temp[i]<=0):
        list_predict_sunspots.append(0)
    else:
        list_predict_sunspots.append(list_temp[i])
plt.figure(figsize=(10, 7))
plt.plot(data['today_confirm'],label='actual value')
plt.plot([i for i in range(4,24,1)],list_predict_sunspots,label='Predictive value')
plt.xticks([i for i in range(0,26,2)])
plt.yticks([i for i in range(-20,40,5)])
plt.xlabel('sequentially',font)
plt.ylabel('Number of newly confirmed cases',font)
#设置网格线及其参数
plt.grid(axis='y',ls=':',c='black',alpha=0.7)
plt.grid(axis='x',ls=':',c='black',alpha=0.7)
plt.legend(prop=font)
residuals.plot(kind='kde')
plt.show()

results.forecast()[0]




