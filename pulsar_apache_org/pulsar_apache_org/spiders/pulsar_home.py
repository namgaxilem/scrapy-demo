import scrapy


class PulsarHomeSpider(scrapy.Spider):
    name = "pulsar_home"
    allowed_domains = ["pulsar.apache.org"]
    start_urls = ["https://pulsar.apache.org"]

    def parse(self, response):
        pass
