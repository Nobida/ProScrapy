# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JdspiderPipeline(object):

    def __init__(self):
        self.client = pymysql.connect(
            host='59.110.243.182',
            port=3306,
            user='root',  #使用自己的用户名
            passwd='qzwkx333530',  # 使用自己的密码
            db='restframework',  # 数据库名
            charset='utf8'
        )
        self.db_cur = self.client.cursor()

    def process_item(self,item,spider):
#        insert_sql = '''
#                      INSERT INTO JD_items_copy(`product_id`,`category_id`,`product_name`,`shop_id`) VALUES ('%s','%d','%s','%s')
#                     '''%(item['product_id'],item['category_id'],item['product_name'],item['shop_id'])
        insert_sql1 = '''
                      INSERT INTO JD_item_price(`product_id`,`price`,`date`) VALUES ('%s','%s','%s')
                     '''%(item['product_id'],item['price'],item['date'])  
        insert_sql2 = '''
                      INSERT INTO JD_item_sales_volume(`product_id`,`sales_volume`,`date`) VALUES ('%s','%s','%s')
                     '''%(item['product_id'],item['sales_volume'],item['date'])                                        
        #print(insert_sql)
        try:
            #self.db_cur.execute(insert_sql)
            self.db_cur.execute(insert_sql1)
            self.db_cur.execute(insert_sql2)
            self.client.commit()
            print("获取%s最新信息成功"%(item['product_id']))
        except Exception as e:
            print('---')
            print(insert_sql)
            print(e)

class JdspiderPipelineShops(object):

    def __init__(self):
        self.client = pymysql.connect(
            host='59.110.243.182',
            port=3306,
            user='root',  #使用自己的用户名
            passwd='qzwkx333530',  # 使用自己的密码
            db='restframework',  # 数据库名
            charset='utf8'
        )
        self.db_cur = self.client.cursor()

    def process_item(self,item,spider):
        insert_sql = '''
                      INSERT INTO JD_shop(`shop_id`,`shop_name`,`division_id`) VALUES ('%s','%s','%d')
                     '''%(item['shop_id'],item['shop_name'],item['division_id'])
        #print(insert_sql)
        try:
            self.db_cur.execute(insert_sql)
            self.client.commit()
            print("获取%s最新信息成功"%(item['shop_id']))

        except Exception as e:
            print('---')
            print(insert_sql)
            print(e)

class JdspiderPipelineItemPrice(object):

    def __init__(self):
        self.client = pymysql.connect(
            host='59.110.243.182',
            port=3306,
            user='root',  #使用自己的用户名
            passwd='qzwkx333530',  # 使用自己的密码
            db='restframework',  # 数据库名
            charset='utf8'
        )
        self.db_cur = self.client.cursor()

    def process_item(self,item,spider):
        print('-----')
        print("价格")
        print(item)
        print('-----')
        insert_sql = '''
                      INSERT INTO JD_item_price(`product_id`,`price`,`date`) VALUES ('%s','%s','%s')
                     '''%(item['product_id'],item['price'],item['date'])
        #print(insert_sql)
        try:
            self.db_cur.execute(insert_sql)
            self.client.commit()
            print("获取%s价格信息成功"%(item['product_id']))

        except Exception as e:
            print('---')
            print(insert_sql)


class JdspiderPipelineItemVolume(object):

    def __init__(self):
        self.client = pymysql.connect(
            host='59.110.243.182',
            port=3306,
            user='root',  #使用自己的用户名
            passwd='qzwkx333530',  # 使用自己的密码
            db='restframework',  # 数据库名
            charset='utf8'
        )
        self.db_cur = self.client.cursor()

    def process_item(self,item,spider):
        insert_sql = '''
                      INSERT INTO JD_item_sales_volume(`product_id`,`sales_volume`,`date`) VALUES ('%s','%s','%s')
                     '''%(item['product_id'],item['sales_volume'],item['date'])
        #print(insert_sql)
        try:
            self.db_cur.execute(insert_sql)
            self.client.commit()
            print("获取%s销量成功"%(item['product_id']))

        except Exception as e:
            print('---')
            print(insert_sql)            
            print(e)            

class JdspiderPipelineItemDatePrice(object):

    def __init__(self):
        self.client = pymysql.connect(
            host='59.110.243.182',
            port=3306,
            user='root',  #使用自己的用户名
            passwd='qzwkx333530',  # 使用自己的密码
            db='restframework',  # 数据库名
            charset='utf8'
        )
        self.db_cur = self.client.cursor()

    def process_item(self,item,spider):
        insert_sql = '''
                      INSERT INTO JD_items_datePrice(`product_id`,`price`,`date`,`campaign`) VALUES ('%s','%s','%s','%s')
                     '''%(item['product_id'],item['price'],item['date'],item['campaign'])
        #print(insert_sql)
        try:
            self.db_cur.execute(insert_sql)
            self.client.commit()
            print("获取%s销量成功"%(item['product_id']))

        except Exception as e:
            print('GG BOND')         

