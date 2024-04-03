import scrapy
from site_search_poc.items import SiteSearchPocItem

class PocCrawlSpider(scrapy.Spider):
    name = "poc-crawl"
    allowed_domains = ["scrapingclub.com"]
    def start_requests(self):
        url = "https://scrapingclub.com/exercise/list_infinite_scroll/"
        yield scrapy.Request(url, meta={
                "playwright": True,
                "playwright_context_kwargs": {
                    "ignore_https_errors": True,
                },
            })

    def parse(self, response):
        context = SiteSearchPocItem()
        context['url'] = response.url
        context['title'] = response.css("title::text").get()
        context['metaDescription'] = response.xpath('//meta[@name="description"]/@content').extract_first()
        paragraphs = []
        for p in response.css("p::text").getall():
            p1 = p.strip()
            if len(p1) !=0 :
                paragraphs.append(p1.replace("\n", ""))
        context['paragraphs'] = paragraphs
        yield context
