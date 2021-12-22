# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:51:40 2020

@author: CEB
"""

import json
import requests
import pandas as pd
import csv

# 抓取数据
## 先把数据都爬下来，查看数据结构，明确要整理保存的数据
# url_1包含中国各省市当日实时数据
url_1 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
response_1 = requests.get(url=url_1).json()
data_1 = json.loads(response_1['data'])

# url_2包含中国历史数据及每日新增数据
url_2 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
response_2 = requests.get(url=url_2).json()
data_2 = json.loads(response_2['data'])

lastUpdateTime = data_1["lastUpdateTime"]  # 腾讯最近更新时间
directory = "data_temp_2/" # 定义数据保存路径
# 先保存json文件，以备不时之需

filename1 = directory + lastUpdateTime.split(' ')[0] + "_data_1.json"
with open(filename1, "w", encoding="utf-8") as f:
    f.write(response_1['data'])
    f.close()
filename2 = directory + lastUpdateTime.split(' ')[0] + "_data_2.json"
with open(filename2, "w", encoding="utf-8") as f:
    f.write(response_2['data'])
    f.close()

# d1 = json.load(open(filename1))  # 用于从json文件中读取数据
# d2 = json.load(open(filename2))

# 获取中国当日实时数据
china_data = data_1["areaTree"][0]["children"]
## 获取中国各城市当日实时数据
filename = directory + lastUpdateTime.split(' ')[0] + "_china_city_data.csv"
with open(filename, "w+", encoding="utf_8_sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    header = ["province", "city_name", "total_confirm", "total_nowconfirm", "total_suspect", "total_dead", "total_heal",
              "today_confirm", "lastUpdateTime"]
    writer.writerow(header)
    for j in range(len(china_data)):
        province = china_data[j]["name"]  # 省份
        city_list = china_data[j]["children"]  # 该省份下面城市列表
        for k in range(len(city_list)):
            city_name = city_list[k]["name"]  # 城市名称
            total_confirm = city_list[k]["total"]["confirm"]  # 总确诊病例
            total_nowconfirm = city_list[k]["total"]["nowConfirm"]  # 现存确诊
            total_suspect = city_list[k]["total"]["suspect"]  # 总疑似病例
            total_dead = city_list[k]["total"]["dead"]  # 总死亡病例
            total_heal = city_list[k]["total"]["heal"]  # 总治愈病例
            today_confirm = city_list[k]["today"]["confirm"]  # 今日确诊病例
            data_row = [province, city_name, total_confirm, total_nowconfirm, total_suspect, total_dead,
                        total_heal, today_confirm, lastUpdateTime]
            writer.writerow(data_row)
## 获取中国各省当日实时数据
filename = directory + lastUpdateTime.split(' ')[0] + "_china_province_data.csv"
with open(filename, "w+", encoding="utf_8_sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    header = ["province", "total_confirm", "total_nowconfirm", "total_suspect", "total_dead", "total_heal",
              "today_confirm", "lastUpdateTime"]
    writer.writerow(header)
    for i in range(len(china_data)):
        province = china_data[i]["name"]  # 省份
        total_confirm = china_data[i]["total"]["confirm"]  # 总确诊病例
        total_nowconfirm = china_data[i]["total"]["nowConfirm"]  # 现存确诊
        total_suspect = china_data[i]["total"]["suspect"]  # 总疑似病例
        total_dead = china_data[i]["total"]["dead"]  # 总死亡病例
        total_heal = china_data[i]["total"]["heal"]  # 总治愈病例
        today_confirm = china_data[i]["today"]["confirm"]  # 今日确诊病例
        data_row = [province, total_confirm, total_nowconfirm, total_suspect, total_dead, total_heal, today_confirm, lastUpdateTime]
        writer.writerow(data_row)

# 获取中国历史数据及每日新增数据
chinaDayList = pd.DataFrame(data_2["chinaDayList"])  # 中国历史数据
filename = directory + lastUpdateTime.split(' ')[0] + "_china_history_data.csv"
# header = ["date", "confirm", "suspect", "dead", "heal", "nowConfirm", "nowSevere", "deadRate", "healRate"]
# chinaDayList = chinaDayList[header]  # 重排数据框列的顺序
chinaDayList.to_csv(filename, encoding="utf_8_sig", index=False)

chinaDayAddList = pd.DataFrame(data_2["chinaDayAddList"])  # 中国每日新增数据
filename = directory + lastUpdateTime.split(' ')[0] + "_china_DayAdd_data.csv"
# header = ["date", "confirm", "suspect", "dead", "heal", "deadRate", "healRate"]
# chinaDayAddList = chinaDayAddList[header]  # 重排数据框列的顺序
chinaDayAddList.to_csv(filename, encoding="utf_8_sig", index=False)

# 湖北与非湖北历史数据
def get_data_1():
    with open(filename, "w+", encoding="utf_8_sig", newline="") as csv_file:
        writer = csv.writer(csv_file)
        header = ["date", "dead", "heal", "nowConfirm", "deadRate", "healRate"]  # 定义表头
        writer.writerow(header)
        for i in range(len(hubei_notHhubei)):
            data_row = [hubei_notHhubei[i]["date"], hubei_notHhubei[i][w]["dead"], hubei_notHhubei[i][w]["heal"],
                        hubei_notHhubei[i][w]["nowConfirm"], hubei_notHhubei[i][w]["deadRate"],
                        hubei_notHhubei[i][w]["healRate"]]
            writer.writerow(data_row)

hubei_notHhubei = data_2["dailyHistory"]  # 湖北与非湖北历史数据
for w in ["hubei", "notHubei"]:
    filename = directory + lastUpdateTime.split(' ')[0] + "_" + w + "_history_data.csv"
    get_data_1()

# 获取湖北省与非湖北每日新增数据
hubei_DayAdd = pd.DataFrame(data_2["dailyNewAddHistory"])  # 中国历史数据
filename = directory + lastUpdateTime.split(' ')[0] + "_hubei_notHubei_DayAdd_data.csv"
hubei_DayAdd.to_csv(filename, encoding="utf_8_sig", index=False)

# 获取武汉与非武汉每日新增数据
wuhan_DayAdd = data_2["wuhanDayList"]
filename = directory + lastUpdateTime.split(' ')[0] + "_wuhan_notWuhan_DayAdd_data.csv"
with open(filename, "w+", encoding="utf_8_sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    header = ["date", "wuhan", "notWuhan", "notHubei"]  # 定义表头
    writer.writerow(header)
    for i in range(len(wuhan_DayAdd)):
        data_row = [wuhan_DayAdd[i]["date"], wuhan_DayAdd[i]["wuhan"]["confirmAdd"],
                    wuhan_DayAdd[i]["notWuhan"]["confirmAdd"], wuhan_DayAdd[i]["notHubei"]["confirmAdd"], ]
        writer.writerow(data_row)
