# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collections = table = 'images'
    #有两个属性，分别代表mysel和mongodb存储的表名称
    id = Field()
    url = Field()
    title = Field()
    thumb = Field()
