BOT_NAME = 'walmart_scraper'

SPIDER_MODULES = ['walmart_scraper.spiders']
NEWSPIDER_MODULE = 'walmart_scraper.spiders'

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = { 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None }

CONCURRENT_REQUESTS = 1