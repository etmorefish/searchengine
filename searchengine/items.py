# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchengineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # _id = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    summary = scrapy.Field()
    author = scrapy.Field()
    picUrl = scrapy.Field()
    time = scrapy.Field()
