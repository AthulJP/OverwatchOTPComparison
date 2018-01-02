mkdir SpiderOutput
mkdir Battletags
mkdir PlayerData
virtualenv .
source ./bin/activate
pip install --upgrade pip
pip install scrapy
scrapy startproject Scrapy .
cp Spiders/HeroesSpider.py Scrapy/spiders
cp Spiders/RolesSpider.py Scrapy/spiders
cp Spiders/T100OBSpider.py Scrapy/spiders
cp Spiders/T250MOWSpider.py Scrapy/spiders
