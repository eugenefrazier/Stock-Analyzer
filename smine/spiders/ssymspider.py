import scrapy
import pandas

class QuotesSpider(scrapy.Spider):
    name = "ssym" #Stock symbol

    def start_requests(self):

        yield scrapy.Request(url='https://www.malaysiastock.biz/Listed-Companies.aspx?type=A&value='+input(), callback=self.parse)
        
    def parse(self, response):

        #Extracting the content using css selector

        company_name = response.xpath('//tr/td[@width="250px"]/h3/text()')
        ind_sector = response.xpath('//tr/td[@width="120px"]/h3/text()')
        stock_name = response.xpath('//tr/td/h3/a/text()')



        #Give the extracted content row wise
        for item in range(0,len(stock_name)):
            #create a dictionary to store the scraped info
          
            scraped_info = {
                'stock_symbol':stock_name.extract()[item],
                'company_Name' : company_name.extract()[item],
                'sector' : ind_sector.extract()[item]
                

            }
            
            #yield or give the scraped info to scrapy
            yield scraped_info

    
