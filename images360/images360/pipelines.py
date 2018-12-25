# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Images360Pipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        #它的参数是crawler,通过crawler对象, 我们可以拿到Scrapy的所有核心组件，如全局配置的每个信息
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            user = crawler.settings.get('MYSQL_USER'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT'))

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user,
                                    self.password, self.database, charset = 'utf-8', port = self.port)
        self.cursor = self.db.cursor()


    def close_spider(self, spider):
        #self.db.close()
        pass

    def process_item(self, spider):
        #被定义的item pipeline会默认调用这个方法对item进行处理
        
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        #print(keys)
        #print(values)
##出现问题 
#    yield self.engine.open_spider(self.spider, start_requests)
#AttributeError: 'NoneType' object has no attribute 'encoding'



