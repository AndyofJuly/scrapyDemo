# -*- coding: utf-8 -*-
import scrapy
from Gzgov.items import GzgovItem,DetailsItem
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

            if node.xpath("./a/@href").extract()[0].startswith("../../gzgov/snzc/") :                      
                item['link'] = str("http://www.gz.gov.cn/gzgov/snzc"+"/"+
                    node.xpath("./a/@href").extract()[0].split('/', 5)[4]+"/"+
                    node.xpath("./a/@href").extract()[0].split('/', 5)[5])
            else:
                item['link'] = ""
           # node.xpath("./a/@href").extract()
            
            yield item
            yield scrapy.Request(url=item['link'],callback=self.details)
            
        if self.offset < 67:
            self.offset +=1
            url = self.baseURL + str(self.offset) + self.end
            yield scrapy.Request(url,callback=self.parse)

    def details(self,response):
        item = DetailsItem()
        ps = response.xpath("//div[@class='content_article']/p")        
        item['detail'] = ps.xpath("./text()").extract()
        yield item
        
        #for p in ps:
            #item = DetailsItem()
            #item['detail'] = p.xpath("./text()").extract()
            #yield item
        
#//div[@class='content_article']/p