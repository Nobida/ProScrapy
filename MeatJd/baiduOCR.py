# -*- coding: utf-8 -*-
#import pymysql
#from py2neo import Graph,Node,Relationship,NodeMatcher
#import json
#import re
from aip import AipOcr
from urllib.request import urlretrieve
import os
import pymysql
import requests
import hashlib 
import json
import re

from taobao_utils.settings import DIVISION_DICT


APP_ID = '15864886'
API_KEY = 'Gl16j6u8StTdZhZHozPwtQpK'
SECRET_KEY = 'RgusGGU044g9eC98BcM7mks0sgmHCvva'


class Connect2DB():

    def __init__(self):
        self.host = '59.110.243.182'
        self.db = 'restframework'
        self.user = 'root'
        self.password = 'qzwkx333530'
        #self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def connect_to_db(self):
        connect = pymysql.connect(
            host=self.host,
            db=self.db,
            user=self.user,
            passwd=self.password,
            charset='utf8',
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = connect.cursor()
        return connect, cursor    

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            image =  fp.read()
            return self.client.basicGeneral(image)

    def get_table_data(self, cursor, sql_query):
        cursor.execute(sql_query)
        datas = cursor.fetchall()
        return datas



def words_splice(sentence):
    pull_word_url = 'http://www.pullword.com/process.php'
    post_data = {
     'source':sentence,
     'param1':0.75,
     'param2':1  
    } 
    response = requests.post(pull_word_url, data=post_data)
    response.encoding = 'utf-8'
    pattern = re.compile(r'[\u4E00-\u9FA5]+:\d+.?\d+|[\u4E00-\u9FA5]+:\d+|[A-z]+:\d+.?\d+|[A-z]+:\d+')
    result = re.findall(pattern, response.text, "")
    return result


def string_process(_list):
    string_result_list = []
    pattern = re.compile(r'(.*?):(.*)')
    for item in _list:
        result = re.findall(pattern, item, "")
        string_result_list.append(result[0][0])
    return string_result_list  

def category_data_process(category_data):
    category_id_lst = []
    category_name_lst = []
    for item in category_data:
        category_id_lst.append(item['category_id'])
        category_name_lst.append(item['category_name'])
    return category_id_lst, category_name_lst

def words_result_process(words_result, category_name_lst):
    words_list = []

    index_list = []
    final_dict = {}
    for item in words_result['words_result']:
        if item['words'] != '更多':
            words_list.append(item['words'])
    for word in words_list:
        if word in category_name_lst:
            key = word
            final_dict[key] = []
        else:
            final_dict[key].append(word)   

    return final_dict         
  
def word_splice_process():
    DIVISION_DICT = {}
    for k,v in CATEGORY_DICT.items():
        division_lst = []
        for item in v:
            word_splice_result = words_splice(item)
            string_process_result = string_process(word_splice_result)
            division_lst.extend(string_process_result)
        DIVISION_DICT[k] = division_lst
        print('完成 %s 的处理'%k)

def save_division_to_db(category_id_lst, cursor, connect):
    for category in DIVISION_DICT.keys():
        index = category_name_lst.index(category)
        category_id = category_id_lst[index]
        for division in DIVISION_DICT[category]:
            division_name = division
            insert_sql = 'INSERT INTO taobao_division (category_id, division_name) VALUES (%d,%s)'%(category_id, "'"+division_name+"'")
            try:    
                cursor.execute(insert_sql)
                connect.commit()
                print('成功')
            except Exception as e:
                print(insert_sql)
                print(e)    

def url_data_process(url_data):
    url_list = []
    for i in url_data[0:10]:
        url = 'https://search.jd.com/Search?keyword=' + i['division_name'] + i['category_name']
        url_list.append(url)
    print(url_list)          

    #print(DIVISION_DICT)     


if __name__ == "__main__":
    engine = Connect2DB()
    connect, cursor = engine.connect_to_db()
    sql_query = "select D.division_id,D.division_name,C.category_name from taobao_division as D left join taobao_category as C on D.category_id = C.category_id;"
    url_datas = engine.get_table_data(cursor,sql_query)
    print(url_datas)
    #url_data_process(url_datas)
    #category_id_lst, category_name_lst = category_data_process(category_datas)    
    #save_division_to_db(category_id_lst,cursor,connect)
#    words_result = engine.get_file_content('/users/wangkaixi/desktop/o.png')

#    final_dict = words_result_process(words_result, category_name_lst)
#    print(DIVISION_DICT)
    #word_splice_process()

    #print(words_splice('Yeey350 Alpha Bounce A30 Stan Smith大Air皮蓬KD9'))
    #print(string_process(['alpha:0.920053', 'bounce:0.931674', 'stan:0.857412', 'smith:0.930649', 'air:0.799963', '皮蓬:0.975213']))



#import requests #

## client_id 为官网获取的AK， client_secret 为官网获取的SK
#host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(API_KEY,SECRET_KEY)
#response = requests.get(host)
#if response:
#    print(response.json())

  