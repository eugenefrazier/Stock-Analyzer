# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import os


current_dir = "/home/jin/Desktop/15_04_2019_clairvos_miner_V3/"
base_dir = 'dataset'
dir_raw = 'company_datalist_prefilter'
in_dir = current_dir+base_dir

df = pd.read_csv(current_dir+base_dir+'/'+dir_raw+'/'+dir_raw+"_combined.csv",dtype=str) #Dont forget to change the directory here

class FundbotSpider(scrapy.Spider):
    name = 'Fundbot'
    allowed_domains = ['http:///']
    start_urls = ['http:////']
    
    def start_requests(self):

        for i in range(0,df['stock_code'].count()):
            yield scrapy.Request(url='https://='+str(df["stock_code"][i]), callback=self.parse)

    def parse(self, response):

        company_name = response.xpath("//label[@id='lblCorporatePageTitle']/text()")
        market_cap =    response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_Capital']/text()") 
        num_share  =    response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbNumberOfShare']/text()")
        eps =   response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_EPS']/text()")
        roe =   response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_ROE']/text()")
        pe_ratio =  response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_PE']/text()")
        div =  response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_Div']/text()")
        div_yield =    response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_DY']/text()")
        div_policy =   response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_Policy']/text()")
        nta =   response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_NTA']/text()")
        par_value = response.xpath("//div[@class='corporateInfoValue_FinancialInfo']/label[@id='MainContent_lbFinancialInfo_ParValue']/text()")
    

        scraped_info = {

            'Stock_Symbol': company_name.extract(),
            'market_capital':market_cap.extract(),
            'num_share' : num_share.extract(),
            'eps' : eps.extract(),
            'pe_ratio' : pe_ratio.extract(),
            'roe' : roe.extract(),
            'div' : div.extract(),
            'div_y' : div_yield.extract(),
            'div_p' : div_policy.extract(),
            'nta' : nta.extract(),
            'par_v' : par_value.extract()
        }

        #yield or give the scraped info to scrapy
        yield scraped_info

