import scrapy

class CostaRicaBlogSpider(scrapy.Spider):
    name = 'costa_rica_blog'
    start_urls = ['https://www.liveincostarica.com/blog/articles']

    custom_settings = {
        'FEEDS': {
            'data/%(name)s_%(time)s.json': {
                'format': 'json',
                'fields': ['date', 'title', 'content', 'url'],
            },
        },
    }

    def parse(self, response):

        for article in response.css('.no-post-author'):
            article_url = article.css('.entry-title a::attr(href)').get()
            article_date = article.css('time.post-date::attr(datetime)').get()

            yield response.follow(article_url, self.parse_article, meta={'article_date': article_date})

        next_page = response.css('a.number.nextp::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):

        title = response.css('h1 a::text').get()
        content = response.css('.entry-content p::text').getall()
        date = response.meta['article_date']

        yield {
            'date': date,
            'title': title,
            'content': content,
            'url': response.url
        }