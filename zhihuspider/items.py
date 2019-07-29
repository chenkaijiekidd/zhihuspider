# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZhihuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    token = Field()
    name = Field()
    gender = Field()
    head_line = Field()
    follwer_count = Field()
    avatar_url = Field()
    detail_url = Field()
    locate = Field()
    depth = Field()
    business = Field() #行业
