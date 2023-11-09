import scrapy

class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    start_urls = ['https://ticotimes.net/categories/expats']

    custom_settings = {
    'FEEDS': {
        'data/%(name)s_%(time)s.json': {
            'format': 'json',
            'fields': ['url'],
        },
    },
}

    def parse(self, response):

        for link in response.css('a.td-image-wrap::attr(href)'):
            href = link.get()
            yield {
                'url': href
            }


