# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


class WebCrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def remove_whitespace(value):
    return value.strip()


class JokeItem(scrapy.Item):
    joke_text = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )


class MobileItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    discount = scrapy.Field()
