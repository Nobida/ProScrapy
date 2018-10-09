# -*- coding: utf-8 -*-
import scrapy
from jd.items import JdItem
from scrapy_splash import SplashRequest



lua_script = '''
function main(splash)
    #打开页面
    splash:go(splash.args.url)
    #等待渲染
    splash:wait(2)
    #执行js触发数据加载(后30本书
    splash:runjs("document.getElementsByClassName('page')[0].scrollIntoView(true)")
    #等待渲染
    splash:wait(2)
    #返回html
    return splah:html()
end
'''

class JdSpider(scrapy.Spider):
    """我们需要全部载入网页，然后才能寻找到下一页的链接"""
    name = 'JD'
    finalset = 48
    keyword = '性'

    #allowed_domains = ['https://search.jd.com/Search?keyword=python']
    start_urls = ['https://search.jd.com/Search?keyword={}&enc=utf-8&wq={}'.format(keyword, keyword)]
    print(start_urls)



    def parse(self,response):
        TotalPage = int(response.css('span.fp-text i ::text').extract_first())
        if TotalPage is None:
            print('dsadasdasdasdasd')
        if self.finalset <= TotalPage:
            for i in range(self.finalset):
                url = '%s&page=%s' % (self.start_urls[0], i * 2 + 1)
                yield SplashRequest(url, callback = self.parse_info,
                                endpoint = 'execute',
                                args = {'lua_source' : lua_script},
                                cache_args = ['lua_source'])
        else:
            for i in range(TotalPage):
                url = '%s&page=%s' % (self.base_url, i * 2 + 1)
                yield SplashRequest(url, callback = self.parse_info,
                                endpoint = 'execute',
                                args = {'lua_source' : lua_script},
                                cache_args = ['lua_source'])


    def parse_info(self, response):
        book = JdItem()
        for i in response.css('div.gl-i-wrap'):
            book['Price'] = i.css('div.p-price strong').xpath('string(.)').extract_first()
            book['Name'] = i.css('div.p-name a em').xpath('string(.)').extract_first()
            book['Comment'] = i.css('div.p-commit strong a::text').extract_first()
            book['Store'] = i.css('div.p-shopnum a::text').extract_first()
            yield book
