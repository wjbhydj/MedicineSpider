# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib.parse import urljoin
import re
from scrapy import signals
from selenium import webdriver
from pydispatch import dispatcher
from MedicineSpider.utils import common
from MedicineSpider.items import MedicinespiderItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://mall.jd.com/index-1000015441.html']

    def __init__(self):

        # 设置chromedriver不加载图片
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_opt.add_experimental_option("prefs", prefs)

        self.browser = webdriver.Chrome(executable_path="C:/迅雷下载/chromedriver.exe" ,chrome_options=chrome_opt)
        # self.browser = webdriver.Chrome(executable_path="C:/迅雷下载/chromedriver.exe")
        super(JdSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)


    def spider_closed(self, spider):
        print('spider closed')
        self.browser.quit()

    def parse(self, response):
        item = MedicinespiderItem()
        #商品主分类的图片url
        main_image_cate_url = response.css(".user_rofeyi .cate img::attr(src)").extract_first()
        #商品主分类
        main_cate_list = common.get_cate("https:" + main_image_cate_url)
        #商品主分类url列表
        main_cate_url_list = response.css("#Map_m area::attr(href)").extract()

        x = 0
        # yield Request(url=urljoin(response.url, main_cate_url_list[0]), callback=self.parse_medicine_list,
        #               meta={'item': self.item})

        for second_cate_url in main_cate_url_list[0:1]:
            item['pro_main_cate'] = main_cate_list[x]
            x += 1
            i = 197
            start = 30
            yield Request(url=urljoin(response.url, second_cate_url), callback=self.parse_medicine_list, meta={'item':item, 'i':i, 'start':start})

    #解析药品列表
    def parse_medicine_list(self, response):
        item = response.meta.get('item', "")
        i = response.meta.get('i', "")
        start = response.meta.get('start', "")
        #药品url列表
        medicine_url_list = response.css("#J_goodsList .gl-item .p-img a::attr(href)").extract()
        #请求详情页面
        for medicine_url in medicine_url_list:
            yield Request(url=urljoin(response.url, medicine_url), callback=self.parse_medicine_detail, meta={'item':item})

        #提取下一页的url并交给parse_medicine_list进行解析
        # 构建下一页面的next_url
        next_urls_re = re.match("(.*)?&page", response.url)
        next_urls = next_urls_re.group(1).replace(",", "%2C")

        #提取下一页的class属性
        next_url_class = response.xpath("//div[@id='J_bottomPage']//a[contains(@class,'pn-next')]/@class").extract_first()
        #判断是否为最后一页
        if next_url_class != "pn-next disabled":
            i += 2
            start *= i
            #构建下一页面的next_url
            next_url = next_urls + "&page={i}&s={s}&click=0".format(i=i, s=start)
            yield Request(next_url, callback=self.parse_medicine_list, meta={'item':item, 'i':i, 'start':start})
        else:
            print("next_a:", next_url_class)

    #解析药品详情
    def parse_medicine_detail(self, response):
        item = response.meta.get('item', "")
        #商品编号
        item['pro_nums'] = response.xpath("//ul[@id='parameter-brand']/following-sibling::ul//li/@title")[1].extract()
        #商品价格
        item['pro_price'] = response.xpath("//div[@class='summary-price-wrap']//span[@class='p-price']//span/text()")[1].extract()
        #店铺名称
        item['pro_store'] = response.xpath("//div[@class='contact fr clearfix']//div[@class='name']//a/text()").extract_first()

        keys = response.xpath("//div[@class='Ptable-item']//dl//dl//dt/text()").extract()
        values = response.xpath("//div[@class='Ptable-item']//dl//dl//dd/text()").extract()
        #商品详情
        item['pro_details'] = dict(zip(keys, values))

        print(item)
        yield item
