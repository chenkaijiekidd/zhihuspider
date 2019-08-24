# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : analyse.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

follower_list = pd.read_csv('./follower.csv', dtype={'id': str, '昵称': str, '地区': str, '头像url': str, '性别': str,
                                                   '粉丝数': int, '自我介绍': str, '层次': int})
#男
print('男生:', follower_list[follower_list['性别'] == '1']['id'].count())
#女
print('女生:', follower_list[follower_list['性别'] == '0']['id'].count())
#影响粉丝
print('影响粉丝:', follower_list['粉丝数'].sum())
#一级粉丝数
print('一级粉丝数:', follower_list[follower_list['层次'] == 1]['id'].count())
#二级粉丝数
print('二级粉丝数:', follower_list[follower_list['层次'] == 2]['id'].count())
#二级粉丝数
print('三级粉丝数:', follower_list[follower_list['层次'] == 3]['id'].count())
#地区
print(follower_list.groupby('地区').size())
#行业
print(follower_list.groupby('行业').size())

#性别统计
gender_labels = ['男生', '女生']
male_count = follower_list[follower_list['性别'] == '1']['id'].count()
female_count = follower_list[follower_list['性别'] == '0']['id'].count()
gender_sizes = [male_count, female_count]
gender_explode = (0, 0.1)
plt.pie(gender_sizes, explode=gender_explode, labels=gender_labels, autopct='%1.1f%%', shadow=False, startangle=150)
plt.title("性别比例")
plt.rcParams['font.sans-serif'] = ['Heiti TC'] #用来正常显示中文标签
plt.show()

#转换成字典并且去掉地区为空的数据
area_dict = dict(follower_list.groupby('地区').size())
del area_dict['空']
# 创建一个点数为 20 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(20, 6), dpi=80)
# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)
# 柱子总数
N = len(area_dict.keys())
#按照value排序
area_dict = dict(sorted(area_dict.items(), key=lambda x:x[1], reverse=True))
# 包含每个柱子对应值的序列
values = (area_dict.values())
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.35
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="地区", color="#87CEFA")
# 设置横轴标签
plt.xlabel('地区')
# 设置纵轴标签
plt.ylabel('数量')
# 添加标题
plt.title('地区统计')
# 添加纵横轴的刻度
plt.xticks(index, (area_dict.keys()))
plt.yticks(np.arange(0, 40, 5))
# 添加图例
plt.legend(loc="upper right")
plt.rcParams['font.sans-serif'] = ['Heiti TC'] #用来正常显示中文标签
plt.show()


business_dict = dict(follower_list.groupby('行业').size())
# 创建一个点数为 30 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(30, 6), dpi=80)
# 再创建一个规格为 1 x 1 的子图
plt.subplot(1, 1, 1)
# 柱子总数
N = len(business_dict.keys())
#按照value排序
business_dict = dict(sorted(business_dict.items(), key=lambda x:x[1], reverse=True))
# 包含每个柱子对应值的序列
values = (business_dict.values())
# 包含每个柱子下标的序列
index = np.arange(N)
# 柱子的宽度
width = 0.35
# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="行业", color="#FF7F00")
# 设置横轴标签
plt.xlabel('行业')
# 设置纵轴标签
plt.ylabel('数量')
# 添加标题
plt.title('行业统计')
# 添加纵横轴的刻度
plt.xticks(index, (business_dict.keys()))
plt.yticks(np.arange(0, 40, 5))
# 添加图例
plt.legend(loc="upper right")
plt.rcParams['font.sans-serif'] = ['Heiti TC'] #用来正常显示中文标签
plt.show()