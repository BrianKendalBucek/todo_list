import scrapy

class CostaRicaBlogSpider(scrapy.Spider):
    name = 'costa_rica_blog'
    start_urls = ['https://www.liveincostarica.com/blog/articles']

    custom_settings = {
        'FEEDS': {
            'data/%(name)s_%(time)s.json': {
                'format': 'json',
                'fields': ['date', 'title', 'paragraphs', 'url'],
            },
        },
    }

    def parse(self, response):
        # Find each article entry, extract the date, and follow the link to the article
        for article in response.css('.no-post-author'):
            article_url = article.css('.entry-title a::attr(href)').get()
            article_date = article.css('time.post-date::attr(datetime)').get()

            # Pass the extracted date to the parse_article method
            yield response.follow(article_url, self.parse_article, meta={'article_date': article_date})

        # Find the link to the next page and go there
        next_page = response.css('a.number.nextp::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        # Extract the title and paragraphs of the article
        title = response.css('h1 a::text').get()
        paragraphs = response.css('.entry-content p::text').getall()

        # Retrieve the date passed from the parse method
        date = response.meta['article_date']

        yield {
            'date': date,
            'title': title,
            'paragraphs': paragraphs,
            'url': response.url
        }
