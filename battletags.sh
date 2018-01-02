source ./bin/activate
scrapy crawl Heroes -o SpiderOutput/Heroes.json
scrapy crawl Roles -o SpiderOutput/Roles.json
scrapy crawl T100OB -o SpiderOutput/T100OB.json
scrapy crawl T250MOW -o SpiderOutput/T250MOW.json
python FetchBattletags/heroes.py SpiderOutput/Heroes.json Battletags/Heroes.json
python FetchBattletags/roles.py SpiderOutput/Roles.json Battletags/Roles.json
python FetchBattletags/t100ob.py SpiderOutput/T100OB.json Battletags/T100OB.json
python FetchBattletags/t250mow.py SpiderOutput/T250MOW.json Battletags/T250MOW.json
python FetchBattletags/mergelists.py Battletags/Heroes.json Battletags/Roles.json Battletags/T100OB.json Battletags/T250MOW.json Battletags/Battletags.json

