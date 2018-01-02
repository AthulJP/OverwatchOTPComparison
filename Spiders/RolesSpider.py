import scrapy

class RolesSpider(scrapy.Spider):
    """Spider for scraping the names of the top players of any given role according to Overbuff"""
    name="Roles"
    start_urls = [
        "https://www.overbuff.com/roles/offense/rankings?mode=competitive",
        "https://www.overbuff.com/roles/defense/rankings?mode=competitive",
        "https://www.overbuff.com/roles/tank/rankings?mode=competitive",
        "https://www.overbuff.com/roles/support/rankings?mode=competitive"
    ]


    def parse(self, response):
        """Extract usernames"""
        url = response.url
        for userRow in response.css("table tr"):
            yield{
                url[31:34] : userRow.css('a::attr(href)').extract_first()
            }
