# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class SimpleEnergyItem(Item):
    file_name = Field()
    file_extension = Field()
    file_uri = Field()
    file_content = Field()
    file_path = Field()
