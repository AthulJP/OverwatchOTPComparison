import scrapy

class T100OBSpider(scrapy.Spider):
    """Spider for scraping the names of the top 100 players according to Overbuff"""
    name = "T100OB"
    start_urls = [
        "https://www.overbuff.com/rankings"
    ]

    def parse(self, response):
        """Extract usernames"""
        url = response.url
        for userRow in response.css("table tr"):
            yield{
                'url' : userRow.css('a::attr(href)').extract_first()
            }
        
