# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from tutorial.items import TutorialItem

class TutorialPipeline(object):
    def __init__(self):

        #连接数据库
	print('db connect')
        self.conn=pymysql.Connect(
                host='localhost',
                port=3306,
                db='testdb',
                user='username',
                passwd='passwd~',
                charset='utf8',
                use_unicode=True)
        self.cursor=self.conn.cursor()

    def process_item(self, item, spider):
	print('sql begin')
        print(item['name'][0])
	sql="insert into  testdb.donateDetail (rq,DONATOR, CLASSNAME, MONEYVALUE,project) VALUES ('%d','%s','%s','%f','%s')"
	print('sql:=')
	data=(int(item['donateTime'][0].encode('utf-8').replace('-','')),item['name'][0].encode('utf-8').strip(),item['className'][0].encode('utf-8').strip(),float(item['moneyValue'][0].encode('utf-8').replace('元','')),item['donateProject'][0].encode('utf-8').strip())
	print(data)
	print(int(item['donateTime'][0].encode('utf-8').replace('-','')))
	self.cursor.execute(sql%data)
        self.conn.commit()
        return item
	
    def close_spider(self,spider):
	print('db close')
	self.conn.close()

