# -*- coding: utf-8 -*-
from JDSpider.utils.settings import Connect2DB
from JDSpider.utils.mmm import headers, funJs
from JDSpider.items import JdspiderItem
import json
import scrapy
import execjs
import requests
import copy
import time


class MmmSpider(scrapy.Spider):
    name = 'mmm'


    def __init__(self):
        self.engine = Connect2DB()
        self.connect, self.cursor = self.engine.connect_to_db()
        self.fun1 = execjs.compile(funJs)

    def start_requests(self):
        sql_query = "select * from JD_items_copy limit 40000,5000"
        datas = self.engine.get_table_data(self.cursor,sql_query)
        for data in datas:
            url = 'https://item.jd.com/%s.html'%data['product_id']
            token = self.fun1.call('d.encrypt', url, 2, 1)
            params = {
                'DA': '1',
                'action': 'gethistory',
                'url': url,
                'token': token,
            }
            meta = {}
            meta['token'] = token
            meta['data'] = params
            meta['product_id'] = data['product_id']
            #page = requests.get("http://tool.manmanbuy.com/history.aspx")
            #return json.loads(page.text)            
            #request_url = 'http://tool.manmanbuy.com/history.aspx?DA=1&action=gethistory&url=%s&bjid=&spbh=&cxid=&zkid=&w=951&token=ah5m43e19197789defce36abc258847a239fp63zyn6sy'%url
            #request_url='http://tool.manmanbuy.com/history.aspx?DA=1&action=gethistory&url=https%253A%2F%2Fitem.jd.com%2F'+data['product_id']+'.html&bjid=&spbh=&cxid=&zkid=&w=951&token=pf9b94d4d5593bc387be2685887d2bd33c59s1giz317i'
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)


    def parse(self, response):
        meta = copy.copy(response.meta)
        page = requests.get("http://tool.manmanbuy.com/history.aspx", headers=headers, params=meta['data'])
        content = json.loads(page.text)
        datePrices = eval('['+content['datePrice']+']')
        for datePrice in datePrices:
            item = JdspiderItem()
            item['date'] = self._time_process(datePrice[0])
            item['product_id'] = meta['product_id']
            item['price'] = datePrice[1]
            item['campaign'] = datePrice[2]
            yield item




    def _time_process(self,timeStamp):
        timeStamp = int(str(timeStamp)[0:10])
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        return otherStyleTime







                     