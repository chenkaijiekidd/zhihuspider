# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : pipelines.py
@公众号: 蓝鲸AI教育 bwaiedu
"""
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
#import codecs
import os
import csv
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re
from scrapy.exceptions import DropItem

class ZhihuspiderPipeline(object):

    def __init__(self):
        #self.file = codecs.open(filename='follower.csv', mode='w+', encoding='utf-8')
        csv_file = '../follower.csv'
        self.file = open(csv_file, 'w+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file, dialect="excel")
        #增加表头行
        self.writer.writerow(['id', '昵称', '地区', '行业',  '头像url', '性别', '粉丝数', '自我介绍', '层次'])

    def process_item(self, item, spider):
        # res = dict(item)
        # self.file.write(json.dumps(res, ensure_ascii=False))
        # self.file.write(',\n')
        self.writer.writerow([item['token'], item['name'], item['locate'], item['business'], item['avatar_url'],
                              item['gender'], item['follwer_count'], item['head_line'], item['depth']])
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()

class SaveImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(url=item['avatar_url'], meta={'name': item['token']})

    def item_completed(self, results, item, info):
        if not results[0][0]:
            raise DropItem('下载失败')
        return item

    def file_path(self, request, response=None, info=None):
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 提取url前面名称作为图片名
        image_name = request.url.split('/')[-1]
        # 清洗Windows系统的文件夹非法字符，避免无法创建目录
        filename = re.sub(r'[？\\*|“<>:/]', '', str(name)) + '.jpg'
        return filename
