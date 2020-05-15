# -*- coding: utf-8 -*-

# Scrapy settings for MedicineSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MedicineSpider'

SPIDER_MODULES = ['MedicineSpider.spiders']
NEWSPIDER_MODULE = 'MedicineSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

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
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'MedicineSpider.middlewares.MedicinespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #设置动态生成js页面
   'MedicineSpider.middlewares.JSPageMiddleware': 1,

   #设置随机UserAgent
   # 'MedicineSpider.middlewares.RandomUserAgentMiddleware': 20,
   # # 默认自带用户代理中间件需要none不使用
   # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,

   #使用scrapy_fake_useragent设置随机UserAgent
   # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
   # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
   # 'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,

   #scrapy_crawlera随机代理ip设置
   # 'scrapy_crawlera.CrawleraMiddleware': 60,
   'MedicineSpider.middlewares.MedicinespiderDownloaderMiddleware': 543,
}
#设置随机代理ua
RANDOM_UA_PER_PROXY = True
#禁止fake-useragent无法检索到一个随机的UA字符串发生异常
FAKEUSERAGENT_FALLBACK = None

#scrapy_crawlera随机代理ip设置
CRAWLERA_ENABLED = True
CRAWLERA_APIKEY = 'accf9154b2a947bf9e32dfd9a2ea3096'

CRAWLERA_USER = ''
CRAWLERA_PASS = ''

CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {

   # 使用异步通用方式写入数据库
   # 'MedicineSpider.pipelines.MysqlTwistedPipeline': 20,

   # 将数据写入到elasticsearch当中
   'MedicineSpider.pipelines.ElasticsearchPipeline': 20,

   # 自定义的保存数据到json文件中的pipeline。
   # 'MedicineSpider.pipelines.JsonWithEncodingPipeline': 20,

   # 调用scrapy提供的json export导出json文件
   # 'MedicineSpider.pipelines.JsonExporterPipeline': 10,

   # 使用同步通用方式写入数据库
   # 'MedicineSpider.pipelines.MysqlPipeline': 30,
}

# mysql基本信息
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "jd"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"

RANDOM_UA_TYPE = "random"
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
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
