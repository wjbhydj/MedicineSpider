# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import json

import scrapy

from models.es_jd import MedicineType


class MedicinespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pro_main_cate = scrapy.Field()
    pro_nums = scrapy.Field()
    pro_price = scrapy.Field()
    pro_store = scrapy.Field()
    pro_details = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into medicine(pro_nums,pro_main_cate,pro_price,pro_store)
            VALUES (%s, %s, %s,%s) ON DUPLICATE KEY UPDATE pro_nums=VALUES(pro_nums)
        """
        # self.make_data_clean()
        params = (
            self['pro_nums'],
            self['pro_main_cate'],
            self['pro_price'],
            self['pro_store'],
            # self.pro_details,
        )

        return insert_sql, params

    def save_to_es(self):
        medicine = MedicineType()
        print(self)
        medicine.pro_main_cate = self['pro_main_cate']
        medicine.meta.id = self['pro_nums']
        medicine.pro_price = self['pro_price']
        medicine.pro_store = self['pro_store']
        lines = json.dumps(self['pro_details'], ensure_ascii=False)
        medicine.pro_details = lines

        medicine.save()
