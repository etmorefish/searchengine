# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class SearchenginePipeline(object):

    def open_spider(self, spider):
        client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        connection = client['search']
        self.db = connection['result']

    def process_item(self, item, spider):
        try:
            # print(item)
            self.db.insert(dict(item))
            # print('ok')
        except Exception as e:
            print(e)
            print('数据存储异常.....')

        return item
