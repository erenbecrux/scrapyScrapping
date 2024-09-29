import scrapy
from scrapy.crawler import CrawlerProcess
import json

class PetlebiScrapperSpider(scrapy.Spider):
    name = "petlebi_scrapy"
    allowed_domains = ["petlebi.com"]
    start_urls = ["https://www.petlebi.com/kedi-petshop-urunleri","https://www.petlebi.com/kopek-petshop-urunleri","https://www.petlebi.com/kus-petshop-urunleri","https://www.petlebi.com/kemirgen-petshop-urunleri"]

    def parse(self, response):

        items = response.css("div.card.mb-4")
        for item in items:

            item_page = item.css("div a").attrib["href"]

            itemString = item.css("div a").attrib["data-gtm-product"]
            itemDictionary = json.loads(itemString)
            currentItem = {
                "url" : item.css("div a").attrib["href"],
                "name" : itemDictionary["name"],   
                "price" : itemDictionary["price"],
                "stock" : itemDictionary["dimension2"],       
                "category" : itemDictionary["category"],
                "id" : itemDictionary["id"],
                "brand" : itemDictionary["brand"]
            }

            yield response.follow(item_page,callback=self.parseItemPage,meta=currentItem)


    def parseItemPage(self, response):
        # title: response.css(".product-detail-main h1::text").get()
        # barcode: barcode = response.css("div.tab-pane.active.show.read-more-box div.row.mb-2")[2]
        # barcode: barcode.css("div.col-10.pd-d-v::text").get()
        # price : response.css(".product-detail-main p span::text").get()
        # description: response.css("div.tab-pane.active.show.read-more-box span#productDescription").get().strip("<span id=\"productDescription\">")
        # brand: response.css("div.tab-pane.active.show.read-more-box div.row.mb-2.brand-line span a::text").get()

        possibleBarcodes = response.css("div.tab-content.product-text-area div.row.mb-2")
        barcode = possibleBarcodes[0]
        for div in possibleBarcodes:
            text = div.css("div.col-2.pd-d-t::text").get()
            if text == 'BARKOD':
                barcode = div

        try:
            description = response.css("div.tab-pane.active.show.read-more-box span#productDescription").get().strip("<span id=\"productDescription\">")
        except:
            try:
                description = response.css("div.tab-pane.active.show span#productDescription").get().strip("<span id=\"productDescription\">")
            except:
                description = "No Description"

        yield {

            "url" : response.meta["url"],
            "name" : response.meta["name"],
            "barcode" : barcode.css("div.col-10.pd-d-v::text").get(),
            "price" : response.meta["price"],
            "stock" : response.meta["stock"],
            "description" : description,
            "category" : response.meta["category"],
            "id" : response.meta["id"],
            "brand" : response.meta["brand"]
        }

process = CrawlerProcess(settings={
    "FEEDS": {
        "petlebi_products.json": {"format": "json"},
    },
})

process.crawl(PetlebiScrapperSpider)
process.start()