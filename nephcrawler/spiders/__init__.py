from scrapy.http.request import Request
from scrapy.spiders.crawl import CrawlSpider


DEFAULT_JSON_LD_XPATH = '//script[@type="application/ld+json"]/text()'


class NephilaSpider(CrawlSpider):
    
    def parse_category(self, response):
        yield Request(response.url)


class DmozSpider(NephilaSpider):

    name = "org.dmoz"
    allowed_domains = ['dmoz-odp.org']
    start_urls = ['https://www.dmoz-odp.org']

    def start_requests(self):
        yield Request(self.start_urls[0], 
            callback=self.parse_item)

    def parse_item(self, response):
        yield {
            'description': response.xpath('//meta[@property="og:description"]/@content').get(),
            'image': response.xpath('//meta[@property="og:image"]/@content').get(),
            'name': response.xpath('//meta[@property="og:title"]/@content').get(),
            'keywords': response.xpath('//meta[@name="keywords"]/@content').get()
        }