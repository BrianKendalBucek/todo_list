import scrapy

class TicoSpider(scrapy.Spider):
    name = 'tico_spider'
    start_urls = ['https://ticotimes.net/categories/expats', 'https://ticotimes.net/categories/arts-culture']

    custom_settings = {
    'FEEDS': {
        'data/%(name)s_%(time)s.json': {
            'format': 'json',
            'fields': ['url', 'date', 'title', 'content'],
        },
    },
}

    def parse(self, response):

        for href in response.css('a.td-image-wrap::attr(href)').extract():
            yield response.follow(href, self.parse_article)


    def parse_article(self, response):

        title = response.css('.tdb-title-text::text').get()
        
        date = response.css('.td-module-date::text').get()

        paragraphs = response.css('p::text').extract()

        content = ' '.join(paragraphs)

        yield {
            'title': title,
            'date': date,
            'url': response.url,
            'content': content
        }


