# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import pymysql
from pymysql import cursors
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi
from MedicineSpider.models.es_jd import MedicineType


class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=cursors.Cursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)
        return item

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

    def handle_error(self, failure, item, spider):
        print(failure)

class MysqlPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host ='127.0.0.1',port=3306,user='root',password ='123456',db ='jd',
            charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = '''
            insert into medicine(pro_nums,pro_main_cate,pro_price,pro_store)
            VALUES(%s, %s, %s, %s)
        '''
        self.cursor.execute(
            insert_sql,
            (
                item['pro_nums'],
                item['pro_main_cate'],
                item['pro_price'],
                item['pro_store']
                # item['pro_details']
            )
        )
        self.conn.commit()
        return item


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('medicine.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonExporterPipeline(object):
    def __init__(self):
        self.file = open('medicine_exporter.json', 'wb')
        self.exporter = JsonItemExporter(
            self.file, encoding='utf-8', ensure_ascii=False
        )
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MedicinespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ElasticsearchPipeline(object):
    #将数据写入到ES当中
    def process_item(self, item, spider):

        item.save_to_es()

        return item