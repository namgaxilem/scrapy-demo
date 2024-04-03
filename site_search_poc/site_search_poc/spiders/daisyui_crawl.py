from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PulsarSpider(CrawlSpider):
    name = "daisyui"
    allowed_domains = ["daisyui.com"]
    start_urls = ["https://daisyui.com/docs"]
    base_url = 'https://daisyui.com'
    domain_name = "daisyui.com"
    
    rules = [
        Rule(LinkExtractor(allow='docs/'), callback='parse_docs', follow=True),
        # Rule(LinkExtractor(deny='.*#.*'))
    ]
    
    # custom_settings = {
	# 	'FEEDS': { 
    #         'crawl_data/%(now_year)s/%(now_month)s/%(now_date)s/%(domain_name)s/%(batch_time)s-%(batch_id)d.json': { 
    #             'format': 'json', 
    #             'batch_item_count': 1
    #         }
    #     }
    # }
    
    def start_requests(self):
        url = self.start_urls[0]
        yield Request(url, meta={'playwright': True, "playwright_context_kwargs": {
                    "ignore_https_errors": True,
                },})

    def parse_docs(self, response):
        print(response.url)
        # menuContentList = response.xpath('//*[contains(@class, "menu thin-scrollbar")]/*//a[@href]/text()').extract()
        # for content in menuContentList:
        #     yield {"content": content }
        # links = response.xpath('//*[contains(@class, "theme-doc-sidebar-menu")]/*//a[@href]')
        
        links = response.xpath('//*/a')
        for link in links:
            href = link.xpath('.//@href').extract_first()
            book_url = self.base_url + href
            yield Request(book_url, callback=self.parse_docs) 
        
        url = response.url
        title = response.xpath('//html/head/title/text()').extract_first()
        headings = response.xpath('//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6]/text()').extract()
        metaDescription = response.xpath('//meta[@name="description"]/@content').extract_first()
        
        paragraphs = []
        for p in response.css("p::text").getall():
            p1 = p.strip()
            if len(p1) !=0 :
                paragraphs.append(p1.replace("\n", ""))
        
        yield {
            "url": url,
            "title": title,
            "metaDescription": metaDescription,
            "headings": headings,
            "paragraphs": paragraphs
        }    
