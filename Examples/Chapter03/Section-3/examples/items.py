# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BasicCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link_url = scrapy.Field()
    comment = scrapy.Field()
    location_url = scrapy.Field()
    form = scrapy.Field()
    email = scrapy.Field()

    pass
