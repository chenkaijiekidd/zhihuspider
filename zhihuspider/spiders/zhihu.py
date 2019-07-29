# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
import json
from zhihuspider.items import ZhihuspiderItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    topic_ids = [
        '20190270',  # 长安十二时辰
        #'20230794'  # 亲爱的，热爱的
    ]
    #话题粉丝列表url
    topic_follower_list_url = 'https://www.zhihu.com/api/v4/topics/{0}/followers?include=data%5B%2A%5D.gender%2Canswer_count%2Carticles_count%2Cfollower_count%2Cis_following%2Cis_followed&limit={1}&offset={2}'
    #用户粉丝列表url
    user_follower_list_url = 'https://www.zhihu.com/api/v4/members/{0}/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={1}&limit={2}'
    #用户详细信息url
    detail_info_url = 'https://www.zhihu.com/people/{}/activities'
    #爬取粉丝层数
    crawl_follower_depth = 0

    def start_requests(self):
        '''
        开始爬取热门电视剧
        '''
        for topic in self.topic_ids:
            yield Request(url=self.topic_follower_list_url.format(topic, str(20), str(0)),
                          callback=self.parse_topic_follower, meta={'topic': topic, 'offset': 0})

    def parse_topic_follower(self, response):
        '''
        爬取话题的粉丝，页面上大概只显示150个
        '''
        offset = int(response.meta['offset'])
        res = json.loads(response.text)
        if res['paging']['is_end'] is False and \
                res['data'] is not None and \
                len(res['data']) > 0:
            followers = res['data']
            for follower_data in followers:

                #有部分粉丝没有设置信息公开，不能获取信息则不爬取
                if follower_data['url_token'] is None or follower_data['url_token'] == '':
                    continue

                item = ZhihuspiderItem()
                item['token'] = follower_data['url_token']
                item['avatar_url'] = follower_data['avatar_url'].replace('_is', '_xll')
                item['name'] = follower_data['name']
                item['detail_url'] = self.detail_info_url.format(str(item['token']))
                item['follwer_count'] = follower_data['follower_count']
                item['gender'] = follower_data['gender']
                item['head_line'] = follower_data['headline']
                item['depth'] = 1

                #爬取下一层粉丝
                yield Request(url=self.user_follower_list_url.format(str(item['token']), str(0), str(20)),
                              callback=self.parse_user_follower,
                              meta={'token': item['token'], 'offset': 0, 'depth': 2})

                #爬取第一层粉丝的地区信息
                yield Request(url=item['detail_url'], callback=self.parse_detail_info, meta={'item': item})

            #翻页爬取下一批话题粉丝
            offset += 20
            yield Request(url=self.topic_follower_list_url.format(response.meta['topic'], str(20), str(offset)),
                          callback=self.parse_topic_follower, meta={'topic': response.meta['topic'], 'offset': offset})

    def parse_user_follower(self, response):
        '''
        爬取多层粉丝
        '''
        token = response.meta['token']
        offset = response.meta['offset']
        current_depth = int(response.meta['depth'])

        if current_depth > self.crawl_follower_depth:
            return

        current_depth += 1
        res = json.loads(response.text)
        if res['paging']['is_end'] is False:
            followers = res['data']
            for follower_data in followers:

                #有部分粉丝没有设置信息公开，不能获取信息则不爬取
                if follower_data['url_token'] is None or follower_data['url_token'] == '':
                    continue

                item = ZhihuspiderItem()
                item['token'] = follower_data['url_token']
                item['avatar_url'] = follower_data['avatar_url'].replace('_is', '_xll')
                item['name'] = follower_data['name']
                item['detail_url'] = self.detail_info_url.format(str(item['token']))
                item['follwer_count'] = follower_data['follower_count']
                item['gender'] = follower_data['gender']
                item['head_line'] = follower_data['headline']
                item['depth'] = current_depth

                #爬取粉丝的地区信息
                yield Request(url=item['detail_url'], callback=self.parse_detail_info, meta={'item': item})

                #爬取当前粉丝信息
                yield Request(url=self.user_follower_list_url.format(str(item['token']), str(0), str(20)),
                              callback=self.parse_user_follower,
                              meta={'token': item['token'], 'offset': 0, 'depth': current_depth})

            offset += 20
            #翻页爬取下一批粉丝
            yield Request(url=self.user_follower_list_url.format(str(token), str(offset), str(20)),
                          callback=self.parse_user_follower,
                          meta={'token': token, 'offset': offset, 'depth': current_depth})

    def parse_detail_info(self, response):
        '''
        爬取粉丝的详细信息，主要是地区信息
        '''
        item = response.meta['item']
        selector = Selector(response)
        data = json.loads(selector.xpath('//script[@id="js-initialData"]//text()').extract_first())
        #地区
        try:
            item['locate'] = data['initialState']['entities']['users'][item['token']]['locations'][0]['name']
        except (IndexError, KeyError):
            item['locate'] = '空'
        #行业
        try:
            item['business'] = data['initialState']['entities']['users'][item['token']]['business']['name']
        except (IndexError, KeyError):
            item['business'] = '空'

        yield item

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl('zhihu')
    process.start()
