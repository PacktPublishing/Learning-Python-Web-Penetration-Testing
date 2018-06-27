from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from basic_crawler.items import BasicCrawlerItem
from scrapy.http import Request


class MySpider(BaseSpider):
	name = "basic_crawler"
	allowed_domains = ['packtpub.com']
	start_urls = ["https://www.packtpub.com"]

	def parse(self, response):
		hxs = Selector(response)
		
		#CODE for scraping book titles
		book_titles = hxs.xpath('//div[@class="book-block-title"]/text()').extract()
	 	for title in book_titles:
			book = BasicCrawlerItem()
			book["title"] = title
			yield book 
