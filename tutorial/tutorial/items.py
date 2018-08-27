# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    name=scrapy.Field()
    moneyValue=scrapy.Field()
    className=scrapy.Field()
    donateTime=scrapy.Field()
    donateProject=scrapy.Field()
#    note=scrapy.Field()
