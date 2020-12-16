# -*- coding: utf-8 -*-
from JDSpider.items import JdspiderItem
from JDSpider.utils.settings import URL_LIST
import scrapy
import copy
import re


class MeatjdSpider(scrapy.Spider):
    name = 'MeatJD'


    def start_requests(self):
        for item in URL_LIST:
            url = 'https://search.jd.com/Search?keyword='+item['division_name']+item['category_name']+'&psort=3&click=0'
            yield scrapy.Request(url=url, callback=self.parse, meta=item)

    def parse(self, response):

        pre_item = copy.copy(response.meta)
        
        #product_id_lst  = response.xpath("//ul[@class='gl-warp clearfix']/li/@data-sku").extract()
        division_id = pre_item['division_id']
        #product_name_lst = response.xpath("//div[@class='p-name p-name-type-2']/a/@title").extract()
        shop_id_lst = response.xpath("//div[@class='p-shop']//a[@class='curr-shop hd-shopname']/@href").extract()    
        shop_name_lst  = response.xpath("//div[@class='p-shop']//a[@class='curr-shop hd-shopname']/text()").extract()
        #goods_set = list(zip(product_id_lst,product_name_lst,shop_id_lst,shop_name_lst))
        goods_set = list(zip(shop_id_lst,shop_name_lst))
        for good in goods_set:
            item = JdspiderItem()
            #item['product_id'] = good[0]
            item['division_id'] = int(division_id)
            #item['product_name'] = good[1]
            item['shop_id'] = self._shops_id_process(good[0])
            item['shop_name'] = good[1]


            yield item

    def _shops_id_process(self, string):
        pattern = re.compile(r'//mall.jd.com/index-(.*?).html.*?')
        result = re.findall(pattern,string)
        return result[0]
           
