# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class JdspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_id = Field()
    division_id = Field()
    product_url = Field()
    product_name = Field()
    shop_name = Field()
    shop_id = Field()
    sales_volume = Field()
    price = Field()
    category_id = Field()
    date = Field()
    campaign = Field()
    
    
