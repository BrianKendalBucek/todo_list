import scrapy

class WalmartCostaRicaSpider(scrapy.Spider):
    name = 'walmart_canada'

    slug_list = [
        '/ip/Great-Value-Long-Grain-Enriched-Rice-5-lbs/10315395?from=/search',
        '/ip/Nature-s-Own-Butterbread-Sliced-White-Bread-Loaf-20-oz/10450012?athbdg=L1600&adsRedirect=true'
    ]
    
    custom_settings = {
        'FEEDS': {
            'data/%(name)s_%(time)s.json': {
                'format': 'json',
                'fields': ['name', 'price'],
            },
        },
    }

    def start_requests(self):
        base_url = 'https://www.walmart.com'
        for slug in self.slug_list:
            url = base_url + slug
            yield scrapy.Request(url, self.parse_product)

    def parse_product(self, response):
        name = response.css('#name-title::text').get()
        price = response.css('.inline-flex span::text').get()

        yield {
            'name': name,
            'price': price,
        }
        