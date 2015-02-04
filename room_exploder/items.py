# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RoomExploderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SessionItem(scrapy.Item):
    dept = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field() # course name
    session = scrapy.Field() # e.g. L1, LA1
    instructor = scrapy.Field()
    cover = scrapy.Field()
    code = scrapy.Field() # class code beside section
    timeslots = scrapy.Field()

class CourseItem(scrapy.Item):
    dept = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    credit = scrapy.Field()

class TimeslotItem(scrapy.Item):
    wd = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
    room = scrapy.Field()
