# -*- coding: utf-8 -*-
from JDSpider.utils.settings import Connect2DB
from JDSpider.items import JdspiderItem
import scrapy
import json
import copy
import datetime


class GoodsSpider(scrapy.Spider):
    name = 'Goods'



    def __init__(self):
        self.engine = Connect2DB()
        self.connect, self.cursor = self.engine.connect_to_db()

    def start_requests(self):
        sql_query = "select S.shop_id, C.category_id from JD_shop as S left join JD_division as C on S.division_id = C.division_id limit 10"
        datas = self.engine.get_table_data(self.cursor,sql_query)
        for data in datas:
            url = 'https://diviner.jd.com/diviner?lid=16&lim=6&ec=utf-8&p=509001&sku='+data['shop_id']
            yield scrapy.Request(url=url, callback=self.parse, meta=data)
        

    def parse(self, response):
        #print(response.text)
        html = json.loads(response.text)
        pre_item = copy.copy(response.meta)
        category_id = pre_item['category_id']
        shop_id = pre_item['shop_id']
        for data in html['data']:
            item = JdspiderItem()
            item['product_id'] = data['itemid']
            item['category_id'] = category_id
            item['product_name'] = data['t']
            item['shop_id'] = shop_id
            item['price'] = data['jp']
            item['sales_volume'] = data['w']
            item['date'] = datetime.datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S')
            yield item


        
        
