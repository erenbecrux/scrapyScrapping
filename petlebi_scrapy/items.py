# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PetlebiScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    productURL = scrapy.Field()
    productName = scrapy.Field()
    productBarcode = scrapy.Field()
    productPrice = scrapy.Field()
    productStock = scrapy.Field()
    productDescription = scrapy.Field()
    productCategory = scrapy.Field()
    productID = scrapy.Field()
    productBrand = scrapy.Field()
    pass
