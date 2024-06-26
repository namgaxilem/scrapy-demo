# Scrapy settings for site_search_poc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "site_search_poc"

SPIDER_MODULES = ["site_search_poc.spiders"]
NEWSPIDER_MODULE = "site_search_poc.spiders"
DOWNLOAD_HANDLERS = {
        "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    }
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
} 
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "site_search_poc (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "site_search_poc.middlewares.SiteSearchPocSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "site_search_poc.middlewares.SiteSearchPocDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "site_search_poc.pipelines.SiteSearchPocPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
# FEED_EXPORT_BATCH_ITEM_COUNT = 1
FEED_URI_PARAMS = "site_search_poc.utils.uri_params"

FEEDS = {
    'crawl_data/%(now_year)s/%(now_month)s/%(now_date)s/%(domain_name)s/%(batch_time)s-%(batch_id)d.json': {
        'format': 'json',
        'batch_item_count': 100,
        },
    # 'azure://scrapy0test.blob.core.windows.net/dhp-semantic-search/%(now_year)s/%(now_month)s/%(now_date)s/%(domain_name)s/%(batch_time)s-%(batch_id)d.json': {
    #     'format': 'json',
    #     'batch_item_count': 100,
    #     }
}

# FEED_STORAGES = {'azure': 'scrapy_azure_exporter.AzureFeedStorage'}

# AZURE_ACCOUNT_URL = "https://<your-storage-account-name>.blob.core.windows.net/"
# AZURE_ACCOUNT_KEY = "Account key for the Azure account"
# AZURE_CONNECTION_STRING = 'replace_me_here'

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

REDIS_START_URLS_KEY = 'mycrawler:start_urls'
REDIS_PARAMS = {
    'host': 'scrapy-demo.redis.cache.windows.net',
    'port': 6380,
    'password': '',
}
SCHEDULER_PERSIST = True # Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue' # First-In-First-Out (FIFO) Queue