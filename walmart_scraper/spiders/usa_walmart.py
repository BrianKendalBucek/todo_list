import scrapy

class WalmartSpider(scrapy.Spider):
    name = 'walmart_spider'
    allowed_domains = ['walmart.com']
    start_urls = ['https://www.walmart.com/ip/Great-Value-Long-Grain-Enriched-Rice-5-lbs/10315395?athbdg=L1200']
    

    custom_settings = {
    'FEEDS': {
        'data/%(name)s_%(time)s.json': {
            'format': 'json',
            'fields': ['title', 'price']
        },
    },
}

    def parse(self, response):
      
        title = response.css('#main-title::text').get()
        price = response.css('.inline-flex span::text').get()

        yield {
            'title': title,
            'price': price
        }