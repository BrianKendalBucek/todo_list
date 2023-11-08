import scrapy

class CostaRicaBlogSpider(scrapy.Spider):
    name = 'costa_rica_blog'
    start_urls = ['https://www.liveincostarica.com/blog/articles']

    custom_settings = {
    'FEEDS': {
        'data/%(name)s_%(time)s.json': {
            'format': 'json',
            'fields': ['title', 'paragraphs', 'url'],
        },
    },
}

    def parse(self, response):
        # Find links to each article and iterate over them
        for article in response.css('.entry-title a::attr(href)').getall():
            yield response.follow(article, self.parse_article)

        # Find the link to the next page and go there
        next_page = response.css('a.number.nextp::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        # Extract the title and paragraphs of the article
        title = response.css('h1 a::text').get()
        paragraphs = response.css('.entry-content p::text').getall()

        yield {
            'title': title,
            'paragraphs': paragraphs,
            'url': response.url
        }
