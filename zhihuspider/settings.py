# -*- coding: utf-8 -*-

# Scrapy settings for zhihuspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuspider'

SPIDER_MODULES = ['zhihuspider.spiders']
NEWSPIDER_MODULE = 'zhihuspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': '_xsrf=OFmHDcdLttjo0fVGJZHb031NuI7qjadS; _zap=4e2d017c-5ddd-4db6-ae56-e2dc580413cd; d_c0="ADAnjJEnUA-PTsxeLe6_CZA3Kp5i8qg1YHE=|1555857119"; q_c1=894f1b377d79443b9f9f06355a2ef385|1564044231000|1555857170000; __gads=ID=6815aa5df12824d1:T=1555857225:S=ALNI_MYg9K9HsR9m81iHKr6h2H2H8Azp0Q; __utma=51854390.1387102915.1555857611.1555862671.1564044234.3; __utmz=51854390.1564044234.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/20190270/hot; __utmv=51854390.100-1|2=registration_date=20150109=1^3=entry_date=20150109=1; capsion_ticket="2|1:0|10:1564022696|14:capsion_ticket|44:ODg0ZDVjY2U5MzIyNGNiNGJiNTM5NWFhNzJmZDMxNDI=|3faaaf6abdcc910690fae1b6d59268f2b716659bf59412341954bcd15aebd2ff"; z_c0="2|1:0|10:1564022704|4:z_c0|92:Mi4xV19hOEFBQUFBQUFBTUNlTWtTZFFEeVlBQUFCZ0FsVk5zR1VtWGdCNHBUNV9VRThmM3RySHBLd1Mtb3VKRFFxcmNn|93432aa6d035dd9ebf39a8e2f235aba76116a28a9798ad7c3c3f90c4e2e42197"; tst=r; __utmc=51854390'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuspider.middlewares.ZhihuspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'zhihuspider.middlewares.ProxyDownloadMiddleware': 1,
    'zhihuspider.middlewares.ZhihuspiderDownloaderMiddleware': 2,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuspider.pipelines.ZhihuspiderPipeline': 300,
    'zhihuspider.pipelines.SaveImagePipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IMAGES_STORE = '../avatar'

