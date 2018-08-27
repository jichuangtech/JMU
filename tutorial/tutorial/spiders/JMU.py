# -*- coding: utf-8 -*-
import scrapy
import sys
from tutorial.items import TutorialItem

reload(sys)
sys.setdefaultencoding('utf-8')
class JmuSpider(scrapy.Spider):
    name = 'JMU'
 #   allowed_domains = ['jmu.edu.cn']i
    BASEURL="http://alumni.jmu.edu.cn/onlineDonate/"
    start_urls = ["http://alumni.jmu.edu.cn/onlineDonate/donateDetailedLists.action"]

    def parse(self, response):
#        print('response.body')
#        print(response.body)
        print('node_list')
        node_list=response.xpath('//tr[@height="30"]')
        print (node_list)
        for node in node_list[2:]:
          # print('node')
          # print(node)
            #print(node.xpath("./td[1]/text()").extract())
            item=TutorialItem()
            item['name']=node.xpath("./td[1]/text()").extract()
            item['moneyValue']=node.xpath("./td[2]/text()").extract()
            if node.xpath("./td[3]/text()"):
                item['className']=node.xpath("./td[3]/text()").extract()
            else:
                item['className']='-'
            
            item['donateTime']=node.xpath("./td[4]/text()").extract()
            
            if node.xpath("./td[5]/text()"):
                item['donateProject']=node.xpath("./td[5]/text()").extract()
            else:
                item['donateProject']=node.xpath("./td[5]/a/text()").extract()
        #print('item')
 	    #print(item)
           # item['note']=node.xpath("./td[6]/text()").extract()
            yield item


	#nextPage=response.xpath('//tr[@height="30"]/td[@colspan="8"]/a[contains(text(),"后一页")]')
	nextPage=response.xpath(u"//a[text()='后一页']/@href")
	
	print(nextPage)
	if nextPage:
           nextURL=self.BASEURL + nextPage[0].extract()
	   print(nextURL)
	   yield scrapy.Request(nextURL,callback=self.parse)
	else:
	   print('程序结束')
