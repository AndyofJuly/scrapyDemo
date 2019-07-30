# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GzgovItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    name = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()

class DetailsItem(scrapy.Item):
    detail = scrapy.Field()

