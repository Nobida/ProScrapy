# -*- coding: utf-8 -*-
from JDSpider.utils.settings import Connect2DB
from JDSpider.items import JdspiderItem
import scrapy
import json
import copy
import datetime
import time



class GoodspriceSpider(scrapy.Spider):
    name = 'GoodsPrice'

    def __init__(self):
        self.engine = Connect2DB()
        self.connect, self.cursor = self.engine.connect_to_db()

    def start_requests(self):
        sql_query = "select * from JD_items limit 10"
        datas = self.engine.get_table_data(self.cursor,sql_query)
        for data in datas:
            #url = 'https://item.jd.com/%s.html'%data['product_id']
            #request_url = 'http://tool.manmanbuy.com/history.aspx?DA=1&action=gethistory&url=%s&bjid=&spbh=&cxid=&zkid=&w=951&token=ah5m43e19197789defce36abc258847a239fp63zyn6sy'%url
            request_url='http://tool.manmanbuy.com/history.aspx?DA=1&action=gethistory&url=https%253A%2F%2Fitem.jd.com%2F'+data['product_id']+'.html&bjid=&spbh=&cxid=&zkid=&w=951&token=pf9b94d4d5593bc387be2685887d2bd33c59s1giz317i'
            yield scrapy.Request(url=request_url, callback=self.parse, meta=data)

    def parse(self, response):
        pre_item = copy.copy(response.meta)
        html = json.loads(response.text)

        for price in eval(html['datePrice']):
            item = JdspiderItem()
            item['product_id'] = pre_item['product_id']
            item['date'] = price[0]
            item['price'] = price[1]

            yield item
