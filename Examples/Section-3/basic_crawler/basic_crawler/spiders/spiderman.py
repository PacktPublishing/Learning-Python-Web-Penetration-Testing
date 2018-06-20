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
		#book_titles = hxs.xpath('//div[@class="book-block-title"]/text()').extract()
	 	#for title in book_titles:
		#	book = NinjaCrawlerItem()
		#	book["title"] = title
		#	book["location_url"] = response.url
		#	yield book


		#CODE for scraping Forms
		forms = hxs.xpath('//form/@action').extract()
		for form in forms:
			formy = BasicCrawlerItem()
			formy["form"] = form
			formy["location_url"] = response.url
			yield formy

		#CODE for scraping emails
		emails = hxs.xpath("//*[contains(text(),'@')]").extract()
		for email in emails:
			com = BasicCrawlerItem()
			com["email"] = email
			com["location_url"] = response.url
			yield com


		#CODE for scraping comments
		comments = hxs.xpath('//comment()').extract()
		for comment in comments:
			com = BasicCrawlerItem()
			com["comments"] = comment
			com["location_url"] = response.url
			yield com

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
