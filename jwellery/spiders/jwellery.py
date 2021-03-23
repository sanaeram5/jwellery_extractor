import scrapy

class JwelleryClass(scrapy.Spider):
    name='jwellery'

    start_urls=[
        "https://www.houseofindya.com/zyra/necklace-sets/cat"
    ]

    def parse(self,response):
        for j in response.xpath("//div[@class='catgList']"):
            yield{
                'jwellery_name':j.xpath(".//div[@class='catgName']/p/text()").extract(),
            }

        for jw in response.xpath("//div[@class='catgList']"):
            yield{
                'jwellery_price': jw.xpath(".//div[@class='catgName']/span/text()").extract(),
            }

        for ji in response.xpath("//div[@class='catgList']"):
            yield{
                'jwellery_url': ji.xpath(".//div[@class='catgItem']/img/@src").extract(),
            }
