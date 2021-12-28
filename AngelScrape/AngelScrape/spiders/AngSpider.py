from itemloaders import ItemLoader
import mysql.connector
import scrapy

from AngelScrape.items import AngelscrapeItem
            

# conn = mysql.connector.connect(user="root", host="scrapdb2.crbyejbc1y6i.ap-south-1.rds.amazonaws.com", password="S9K1hfKuWzG3dxt1", database="linkedin")
# cursor = conn.cursor()

# cursor.execute("SELECT name from scraping_company")
# l =[]

# for com in cursor:
    
#     l.append(com[0])

# --e-- list of company from linkedin db --e-- #

class AngSpider(scrapy.Spider):
    name = "Angel"
    
    start_urls = [
       "http://angel.co/search?q=likeminds"
    ]
    handle_httpstatus_list = [301, 200]
    
    def parse(self, response):
        # link1 = response.xpath("//div[@class ='result']/div/a/@href")
        # l1=response.urljoin(link1[0])
        # yield scrapy.Request(url=l1)
        # print("l1")
        # job_section_link = response.xpath("//li[contains(@class ,'styles_component__2Aynt Jobs')]/a/@href")
        # j_l =response.urljoin(job_section_link)
        # yield scrapy.Request(url=j_l)
        for ap_link in  response.xpath("//div[contains(@class ,'styles_component__1_YxE styles_expanded__31zII')]"):
            apply_now = ap_link.xpath("//div[contains(@class ,'styles_component__1_YxE styles_expanded__31zII')]/div/a/@href").extract_first()
            yield {
                'apply_link': apply_now
            }
        # for company in response.xpath("//div[@class ='results-list']"):
        #     l = ItemLoader(item=AngelscrapeItem(),selector=company)
        #     l.add_xpath('company_name',".//div[@class='result']/div[2]/div/a")
        #     yield l.load_item()