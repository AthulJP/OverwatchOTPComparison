import pycurl
import json
from io import BytesIO
import urllib

CurlObj = pycurl.Curl()

BattletagsFile = open('Battletags/Battletags.json', 'r')
BattletagsJson = json.load(BattletagsFile)
BattletagsFile.close()

PlayerArray = []

for i in range(len(BattletagsJson)):

    Buffer = BytesIO()
    CurlObj.setopt(pycurl.WRITEDATA, Buffer)
    Battletag = urllib.quote(BattletagsJson[i].encode('utf-8'))
    BattletagUrl = 'http://localhost:4444/api/v3/u/{}/blob'.format(Battletag)
    CurlObj.setopt(pycurl.URL, BattletagUrl)

    CurlObj.perform()

    body = Buffer.getvalue()
    Buffer.close()
    ProfileJson = json.loads(body)
    if('eu' in ProfileJson):
        ProfileData = ProfileJson['eu']
        Player = [BattletagsJson[i], ProfileData]
        PlayerArray.append(Player)
        print(BattletagsJson[i])
    else:
        print('{} not found'.format(BattletagsJson[i].encode('utf-8')))


CurlObj.close()
OutFile = open('PlayerData/Profiles.json', 'w')
OutFile.write(json.dumps(PlayerArray))
OutFile.close

