# -*- coding: utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from itjuzi.items import ItjuziItem
from scrapy import Request
import scrapy
import re
import time
import random



class JuziSpider(RedisSpider):
    name = 'ITJZ'
    allowed_domains = ['itjuzi.com']

    base_url = 'https://www.itjuzi.com/company/'
    offset = 1500
    start_urls = [base_url + str(offset)]
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "gr_user_id=b2e4a2b7-c8d4-48c9-8211-e1c7d17aecf5; MEIQIA_EXTRA_TRACK_ID=0u6tMBd8BMV4q2NynYeHi2HlQrL; pgv_pvi=4723254272; _uab_collina=150828761032882293811833; _hp2_id.2147584538=%7B%22userId%22%3A%220943152900759367%22%2C%22pageviewId%22%3A%222951415284722025%22%2C%22sessionId%22%3A%224352881315354852%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; _umdata=486B7B12C6AA95F29E7B0D9B986D605826CD9993B21A82EBC9F263904235B135B7AF6C58ADEBF26ECD43AD3E795C914C14A77E2253D6654B6C06D2CE147D0285; _ga=GA1.2.641261107.1506414830; acw_tc=781bad0b15381020316501273e1ef73a2a2ce6376f119141c1baf074e24728; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1538102035,1538811800; _gid=GA1.2.1719855169.1538811800; MEIQIA_VISIT_ID=1BC0VrBJGWTYuYjiZ7gqUYdAUCo; identity=xixireport%40163.com; remember_code=N5So65D5.q; unique_token=422773; paidtype=vip; gr_cs1_f2865de9-20a7-4bb1-b489-f995bb87f7f4=user_id%3A422773; gr_session_id_eee5a46c52000d401f969f4535bdaa78=76766ff6-7b46-457a-b02c-88963d03c876; gr_cs1_76766ff6-7b46-457a-b02c-88963d03c876=user_id%3A422773; gr_session_id_eee5a46c52000d401f969f4535bdaa78_76766ff6-7b46-457a-b02c-88963d03c876=true; session=a07150383133bbaac5aa6ad04d10566bde2365f9; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1538814677",
    "Host": "www.itjuzi.com",
    "If-Modified-Since": "Sat, 06 Oct 2018 08:31:08 GMT",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",}

    # 设置cookie登录的验证
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        items = ItjuziItem()
        print(response.url)
        #items['Name'] = re.findall(r'[\u4e00-\u9fa5|()]+',"".join(response.css('span.title h1::text').extract_first()))[0]
        items['Name'] = response.css('span.title h1::text').extract_first().strip()
        items['Round'] = response.css('span.title span::text').extract_first().strip()
        items['FirstField'] = response.css('a.one-level-tag::text').extract_first()
        items['SecondField'] = response.css('a.two-level-tag::text').extract_first().strip()
        items['FoundTime'] = response.css('div.des-more h3 span::text').extract()[0]

        # 将解析完毕的数据 交给 --引擎 --管道
        yield items
        #ti = random.randint(0.4,0.8)
        time.sleep(0.2)
        while self.offset < 2100:
            self.offset += 1
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url, callback = self.parse, headers = self.headers)
        
