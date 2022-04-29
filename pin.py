import scrapy
import json
import csv

class QuotesSpider(scrapy.Spider):
    name="pincodes"
    def start_requests(self):
        urls=["https://nwcmc.gov.in/ptsearch_data.php?colony=206&houseno=&name=&address=&serno="]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)
    def parse(self,response):
        # Name=response.xpath('/html/body/table//tr/text').extract()
        # print(response.body)
        table=response.xpath('/html/body/table//tr/td/div/div/a/text()').extract()
        sr_no=response.xpath('/html/body/table//tr/td[1]/div/span/text()').extract()
        service_no=response.xpath('/html/body/table//td[3]/div/text()').extract()
        person_Name=response.xpath('/html/body/table//tr/td[4]/div/div/text()').extract()
        address=response.xpath('/html/body/table//tr/td[5]/div/span/text()').extract()
        with open('table.csv','w') as f:
            for Table_data in table:
                f.write(Table_data)
                f.write('\n')    
        with open('srNo.csv','w') as f:
            for srno in sr_no:
                f.write(srno)
                f.write('\n')
        with open('serviceNo.csv','w') as f:
            for serviceno in service_no:
                f.write(serviceno)
                f.write('\n')
        with open('PersonName.csv','w') as f:
            for pName in person_Name:
                f.write(pName)
                f.write('\n')
        with open('Adress.csv','w') as f:
            for adress in address:
                f.write(adress)
                f.write('\n')


        



