import scrapy

class T250MOWSpider(scrapy.Spider):
    """Scraper for getting the Top 500 OW players according to MasterOverwatch"""
    name="T250MOW"
    start_urls = [
        'http://localhost:8000/MOWLeaderboard.html'
    ]

    def parse(self, response):
        """Extract usernames"""
        for userLink in response.css('.table-row-link'):
            yield {
                'url':userLink.css('a::attr(href)').extract_first()
            }
