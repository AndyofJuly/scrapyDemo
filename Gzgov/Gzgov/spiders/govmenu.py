# -*- coding: utf-8 -*-
import scrapy
from Gzgov.items import GzgovItem
#from scrapy.http import Request

class GovmenuSpider(scrapy.Spider):
    name = 'govmenu'
    allowed_domains = ['gz.gov.cn']
    #start_urls = ['http://www.gz.gov.cn/gzgov/snzc/common_list.shtml']
    baseURL = "http://www.gz.gov.cn/gzgov/snzc/common_list_"
    offset = 1
    end = ".shtml"
    start_urls = ["http://www.gz.gov.cn/gzgov/snzc/common_list.shtml"]

    def parse(self, response):
        node_list = response.xpath("//ul[@class='news_list']/li")

        for node in node_list:

            item = GzgovItem()

            item['name'] = node.xpath("./a/text()").extract()
            item['time'] = node.xpath("./span/text()").extract()
            item['link'] = node.xpath("./a/@href").extract()
            
            yield item
            
        if self.offset < 66:
            self.offset +=1
            url = self.baseURL + str(self.offset) + self.end
            yield scrapy.Request(url,callback=self.parse)
            
