# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from team.items import TeamItem
from scrapy import Request
import scrapy
import re



class HupuSpider(scrapy.Spider):
    name = 'HUPU'

    start_urls = ['https://nba.hupu.com/teams/']

    def parse(self, response):
        """爬取所有球队的链接"""
        le = LinkExtractor(restrict_css = 'div.team')
        for link in le.extract_links(response):
            yield Request(link.url, callback = self.parse_team)

    def parse_team(self, response):
        """爬取教练及球队两个信息"""
        Team = TeamItem()
        #正则：去除‘主教练：’这一内容，仅保留主教练的名字
        Team['HeadCoach'] = ''.join(re.findall(r'[^主教练：].*?',response.xpath('//div[@class="font"]/p[4]/text()').extract_first()))
        Team['Team'] = response.xpath('//span[@class="title-text"]/text()').extract_first()
        PlayerUrl = response.xpath('//span[@class="crumbs-link"]/a[2]/@href').extract_first()

        #meta参数可以把之前收集到的信息传递到新请求里
        yield Request(PlayerUrl,meta={'item': Team}, callback = self.parse_info)

    def parse_info(self, response):
        """爬取球员信息"""
        #接受上级已经爬取的数据
        Team = response.meta['item']
        for item in response.css('tr')[1:]:
            #同时抓取双子节点，用','隔开 
            data = item.css('td.left b a,p')
            Team['Name'] = data.xpath('string(.)').extract()
            Team['Number'] = item.css('td:nth-child(3)::text').extract_first()
            Team['Position'] = item.css('td:nth-child(4)::text').extract_first()
            Team['Birthday'] = item.css('td:nth-child(7)::text').extract_first()

        #yield Team 注意yield的位置！若yield在该注释处，则返回的将是每队最后一位球员的信息，而非全部球员的信息
            yield Team

