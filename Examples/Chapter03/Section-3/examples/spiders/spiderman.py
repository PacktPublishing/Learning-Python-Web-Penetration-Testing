from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from basic_crawler.items import BasicCrawlerItem
from scrapy.http import Request
import re


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


		visited_links=[]
		links = hxs.xpath('//a/@href').extract()
                link_validator= re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")


		
		for link in links:
			if link_validator.match(link) and not link in visited_links:
				visited_links.append(link)
				yield Request(link, self.parse)
			else:
				full_url=response.urljoin(link)
				visited_links.append(full_url)
				yield Request(full_url, self.parse)
