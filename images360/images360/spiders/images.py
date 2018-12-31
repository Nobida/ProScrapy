# -*- coding: utf-8 -*-
#该句会被解释器解释


from scrapy import Spider, Request
from urllib.parse import urlencode
from images360.items import Images360Item
import json


class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    #允许执行的url范围是：images.so.com
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {'ch':'video','src':'tujiebanner'}
        base_url = 'http://images.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)
    
    def parse(self, response):
        result = json.loads(response.text)
        print("---------------")
        if isinstance(result['list'],list):
        #print(result.get('list'))
        #print(type(result['list']))
            for image in result.get('list'):
    
                item = Images360Item()
                item['id'] = image.get('imageid')
                item['url'] = image.get('qhimg_url')
                item['title'] = image.get('group_title')
                item['thumb'] = image.get('qhimg_thumb_url')
                #print(item)
                yield item
       
