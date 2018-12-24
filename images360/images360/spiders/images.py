# -*- coding: utf-8 -*-
#该句会被解释器解释


from scrapy import Spider, Request
from urllib.parse import urlencode


class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    #允许执行的url范围是：images.so.com
    start_urls = ['http://images.so.com/']

    def parse(self, response):
        data = {'ch':'video','src':'tujiebanner'}
        base_url = 'http://images.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)
        #'https://image.so.com/zj?ch=video&src=tujiebanner&sn={}&listtype=new&temp=1'
       
