import scrapy

class HeroesSpider(scrapy.Spider):
    """Spider for scraping the names of the top players of any given hero accoring to Overbuff"""
    name = "Heroes"
    start_urls = [
        "https://www.overbuff.com/heroes/mercy/rankings",
        "https://www.overbuff.com/heroes/dva/rankings",
        "https://www.overbuff.com/heroes/reinhardt/rankings",
        "https://www.overbuff.com/heroes/zenyatta/rankings",
        "https://www.overbuff.com/heroes/zarya/rankings",
        "https://www.overbuff.com/heroes/junkrat/rankings",
        "https://www.overbuff.com/heroes/genji/rankings",
        "https://www.overbuff.com/heroes/mccree/rankings",
        "https://www.overbuff.com/heroes/moira/rankings",
        "https://www.overbuff.com/heroes/soldier76/rankings",
        "https://www.overbuff.com/heroes/lucio/rankings",
        "https://www.overbuff.com/heroes/roadhog/rankings",
        "https://www.overbuff.com/heroes/winston/rankings",
        "https://www.overbuff.com/heroes/pharah/rankings",
        "https://www.overbuff.com/heroes/ana/rankings",
        "https://www.overbuff.com/heroes/tracer/rankings",
        "https://www.overbuff.com/heroes/reaper/rankings",
        "https://www.overbuff.com/heroes/hanzo/rankings",
        "https://www.overbuff.com/heroes/widowmaker/rankings",
        "https://www.overbuff.com/heroes/orisa/rankings",
        "https://www.overbuff.com/heroes/symmetra/rankings",
        "https://www.overbuff.com/heroes/torbjorn/rankings",
        "https://www.overbuff.com/heroes/bastion/rankings",
        "https://www.overbuff.com/heroes/mei/rankings",
        "https://www.overbuff.com/heroes/sombra/rankings",
        "https://www.overbuff.com/heroes/doomfist/rankings"
    ]

    def parse(self, response):
        """Extract usernames"""
        url = response.url
        for userRow in response.css("table tr"):
            yield{
                url[32:(len(url)-9)] : userRow.css('a::attr(href)').extract_first()
            }
        
