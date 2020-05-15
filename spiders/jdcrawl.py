# -*- coding: utf-8 -*-
import scrapy
from pydispatch import dispatcher
from scrapy import signals
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver


class JdcrawlSpider(CrawlSpider):
    name = 'jdcrawl'
    allowed_domains = ['jd.com']
    start_urls = ['https://mall.jd.com/index-1000015441.html']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def __init__(self):

        # 设置chromedriver不加载图片
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_opt.add_experimental_option("prefs", prefs)

        self.browser = webdriver.Chrome(executable_path="C:/迅雷下载/chromedriver.exe" ,chrome_options=chrome_opt)
        # self.browser = webdriver.Chrome(executable_path="C:/迅雷下载/chromedriver.exe")
        super(JdcrawlSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        print('spider closed')
        self.browser.quit()

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
