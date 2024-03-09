import scrapy
from chocolate_web.items import ChocolateWebItem

class ChocolateSpider(scrapy.Spider):
    name = "chocolate"
    allowed_domains = ["www.chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        item = ChocolateWebItem()
        for product in response.css('.product-item .product-item__info   '):
        
            item['name'] = product.css('.product-item-meta a::text').get()
            item['price'] = product.css('.price-list .price::text')[1].get()

            yield item

            # yield {
            #     'name' : product.css('.product-item-meta a::text').get(),
            #     'price' : product.css('.price-list .price::text')[1].get()
            # }

        next_page = response.css('[rel=next]::attr(href)').get()
        
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, self.parse)
        
        # for i in range(2,5):
        #     next_page_url = 'https://www.chocolate.co.uk/collections/all?page=' + str(i)
        #     yield response.follow(next_page_url, self.parse)



