# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ItjuziItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = Field() #项目名
    Round = Field() #轮次
    FirstField = Field() #一级领域
    SecondField = Field() #二级领域
    City = Field() #城市
    FoundTime = Field() #成立时间
    MoneyTime = Field() #融资时间
    MoneyRound = Field() #融资轮次
    Money = Field() #融资金额
    InvestCompany = Field() #投资机构