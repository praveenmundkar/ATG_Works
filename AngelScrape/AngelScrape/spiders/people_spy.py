import scrapy
import time

class spider5(scrapy.Spider):
    name = "spider5"
    # domain = "https://angel.co/search?q="
    url_list =['https://angel.co/u/surya-grover-1', 'https://angel.co/location/karnataka-d-group-employees-layout', 'https://angel.co/company/limetray', 'https://angel.co/u/lingerie-realm', 'https://angel.co/company/gokukom-digital-agency', 'https://angel.co/company/amdocs-19', 'https://angel.co/company/sheeko', 'https://angel.co/company/tata-consultancy-services', 'https://angel.co/u/hiredigital-1', 'https://angel.co/company/junio_in', 'https://angel.co/company/hike', 'https://angel.co/u/vinayak-managuli', 'https://angel.co/company/sunlight', 'https://angel.co/company/magicpin-1', 'https://angel.co/company/gyandhan', 'https://angel.co/company/clickpost', 'https://angel.co/company/barclays-plc', 'https://angel.co/company/annarabinkov', 'https://angel.co/company/sogeti', 'https://angel.co/company/sunny-corp', 'https://angel.co/location/kivioli', 'https://angel.co/location/bold-springs', 'https://angel.co/u/pauline-houston', 'https://angel.co/location/sheep-ranch', 'https://angel.co/company/appwharf', 'https://angel.co/company/sentieo', 'https://angel.co/company/sb-innovations-web-development', 'https://angel.co/p/stephanie-palmeri', 'https://angel.co/company/360-digital-idea', 'https://angel.co/company/swiggy', 'https://angel.co/company/thrivepass-1', 'https://angel.co/p/rick-zullo', 'https://angel.co/company/transunion', 'https://angel.co/u/arslan-unops-ishaq', 'https://angel.co/u/ken-karnes', 'https://angel.co/u/aj-expertize', 'https://angel.co/location/blackhawk-1', 'https://angel.co/company/microsoft', 'https://angel.co/location/menlo-park', 'https://angel.co/u/ankur-choudhury-2', 'https://angel.co/location/incline-1', 'https://angel.co/company/dimagi-3', 'https://angel.co/company/upguard', 'https://angel.co/u/nancy-lambert-m-s-crc-cft-cdac', 'https://angel.co/location/shelby-shelby-county', 'https://angel.co/u/kd-khairah', 'https://angel.co/company/leena_ai', 'https://angel.co/company/vmware-17', 'https://angel.co/location/global-nagar', 'https://angel.co/company/taxmann', 'https://angel.co/location/bechtelsville', 'https://angel.co/u/bonds-india-1', 'https://angel.co/u/mark-lobo', 'https://angel.co/company/stashfin-1', 'https://angel.co/u/deepansh-nagaria', 'https://angel.co/company/ibm-17', 'https://angel.co/u/jake-stott', 'https://angel.co/location/instrumentation-limited-colony', 'https://angel.co/company/statusneo-1', 'https://angel.co/company/red-hat', 'https://angel.co/u/kabil-raj', 'https://angel.co/u/boriel', 'https://angel.co/u/austinheap', 'https://angel.co/u/kartik-raja-s', 'https://angel.co/p/bernhard-gold', 'https://angel.co/u/infinity-solutions-3', 'https://angel.co/location/hindustan-1', 'https://angel.co/location/gemini-le', 'https://angel.co/company/cashkaro-com', 'https://angel.co/company/rightinfotech', 'https://angel.co/u/akanksha-kumar-7', 'https://angel.co/p/marcobergmann', 'https://angel.co/u/work-sure', 'https://angel.co/company/ethx', 'https://angel.co/u/market-xcel-data-matrix-pvt-ltd-1', 'https://angel.co/u/jessica-baresi', 'https://angel.co/company/the-looma-project', 'https://angel.co/company/grapeseed', 'https://angel.co/u/sahadi-sharma', 'https://angel.co/location/media-pa', 'https://angel.co/u/vikram-joshi-2', 'https://angel.co/location/linkoping', 'https://angel.co/company/octopuscity', 'https://angel.co/company/paytm-10', 'https://angel.co/company/watermelon-hq', 'https://angel.co/location/instrumentation-limited-colony', 'https://angel.co/location/frogner', 'https://angel.co/location/monkey-bay', 'https://angel.co/u/narendra-yadav', 'https://angel.co/u/big-small-3', 'https://angel.co/company/unacademy', 'https://angel.co/company/simulanis-1', 'https://angel.co/u/vidyamarihemanth1', 'https://angel.co/u/namrata-dutta-poly', 'https://angel.co/location/mobile-1', 'https://angel.co/u/digitally-up-1', 'https://angel.co/location/livingston-livingston-parish', 'https://angel.co/company/healthmug', 'https://angel.co/u/rupesh-jain-5', 'https://angel.co/company/mx-player-1', 'https://angel.co/location/maker-saran', 'https://angel.co/p/charles-shyer', 'https://angel.co/company/webgross', 'https://angel.co/company/vizexperts-india-pvt', 'https://angel.co/company/bharatpe', 'https://angel.co/location/india', 'https://angel.co/location/city-s-prime-health-care-area', 'https://angel.co/location/asian-games-village-complex', 'https://angel.co/location/pelham-new-york', 'https://angel.co/company/socialize-india', 'https://angel.co/company/interactive-bees-3', 'https://angel.co/company/monkhub', 'https://angel.co/location/morteau', 'https://angel.co/location/tierra-verde-1', 'https://angel.co/company/the-financialists-singapore-1', 'https://angel.co/u/getz-destinations', 'https://angel.co/location/brandstatt', 'https://angel.co/company/startxlabs', 'https://angel.co/location/aidlingen', 'https://angel.co/u/red-logics', 'https://angel.co/company/blu-cliff', 'https://angel.co/company/uncap-research-labs', 'https://angel.co/u/shahnawaz-1', 'https://angel.co/company/boult-audio', 'https://angel.co/location/media-pa', 'https://angel.co/location/info-technology-park', 'https://angel.co/location/jetpur', 'https://angel.co/u/manju-kaushal', 'https://angel.co/location/innovation-residential-district', 'https://angel.co/u/macwill-information-systems-pvt-ltd', 'https://angel.co/u/athar-hussain-2', 'https://angel.co/location/infraestructura-urbana-plaza-colima', 'https://angel.co/company/alertus-technologies-1', 'https://angel.co/company/iotfy', 'https://angel.co/location/india', 'https://angel.co/location/gurgaon-hr', 'https://angel.co/company/mitra', 'https://angel.co/location/homestead', 'https://angel.co/u/reliance-jio-infocomm-limited-rjil-2', 'https://angel.co/location/state-college', 'https://angel.co/u/nkg-abc', 'https://angel.co/u/sylvain-roussy', 'https://angel.co/location/sisak', 'https://angel.co/company/dell', 'https://angel.co/u/sylvia-coman', 'https://angel.co/u/kuldeep-yadav-1', 'https://angel.co/location/karnataka-d-group-employees-layout', 'https://angel.co/location/knowledge-park-v', 'https://angel.co/location/hrbr-layout', 'https://angel.co/location/indore-mp']

    def start_requests(self,  company_list= url_list):
        for i in company_list:
            time.sleep(3)
            yield scrapy.Request(url=i + '/people',callback = self.parse)

    def parse(self, response):
        
        for founder in  response.xpath("//div[contains(@class,'styles_component__ivX7J styles_twoColumn__XlBrn')]"):
            name = founder.xpath(".//div/div/div/div/div/h4/a/text()").extract_first()
            url = founder.xpath(".//div/div/div/div/div/h4/a/@href").extract_first()
            desc = founder.xpath(".//div/div/div[2]")
            yield {
                "founder":[name, url, desc]
            }
        
        for team in response.xpath("//div[contains(@class,'styles_component__1WTsC styles_box__4RMl8 styles_flexColumn__1dh8k')][2]/div"):
            name = team.xpath(".//div/div/div/div/div/h4/a/text()")
            url = team.xpath(".//div/div/div/div/div/h4/a/@href")
            desc = team.xpath(".//div/div/div/div[2]")
            if desc is not None:
                yield {
                "team" : [name, url, desc]
                }
            else:
                yield {
                    "team" : [name, url, "null"]
                }
        
        for former_team in response.xpath("//div[@class='styles_component__1WTsC styles_box__4RMl8 styles_flexColumn__1dh8k'][3]/div"):
            name = former_team.xpath(".//div/div/div/div/div/h4/a/text()")
            url = former_team.xpath(".//div/div/div/div/div/h4/a/@href")
            position = former_team.xpath(".//div/div/div/div/div/span/text()")
            
            yield {
                "former team" : [name, url, position]
            }