# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def RemoveWhitespace(value):
    return value.strip()

class AngelscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field(
         input_processor= MapCompose(RemoveWhitespace),
        output_processor = TakeFirst()
    )


