import json
import urllib
import sys
import os.path

if(len(sys.argv) != 6):
    print("Usage: python mergelists.py <T250 file> <T100 file> <Roles file> <Heroes file> <All battletags file>")
    sys.exit()

T250File = open(sys.argv[1], 'r')
T100File = open(sys.argv[2], 'r')
RolesFile = open(sys.argv[3], 'r')
HeroesFile = open(sys.argv[4], 'r')

T250Json = json.load(T250File)
T100Json = json.load(T100File)
RolesJson = json.load(RolesFile)
HeroesJson = json.load(HeroesFile)

T250File.close()
T100File.close()
RolesFile.close()
HeroesFile.close()

BattletagList = []

if(os.path.exists(sys.argv[5])):
    BattletagsFile = open(sys.argv[5], 'r')
    BattletagsJson = json.load(BattletagsFile)
    BattletagList = BattletagsJson[0:]    
    BattletagsFile.close()


for i in range(len(T100Json)):
    if((not(' ' in T100Json[i])) and (not('\t' in T100Json[i])) and ('-' in T100Json[i])):
        if(not (T100Json[i] in BattletagList)):
            BattletagList.append(T100Json[i])

for i in range(len(RolesJson)):
    if((not(' ' in RolesJson[i])) and (not('\t' in RolesJson[i])) and ('-' in RolesJson[i])):
        if(not (RolesJson[i] in BattletagList)):
            BattletagList.append(RolesJson[i])

for i in range(len(HeroesJson)):
    if((not(' ' in HeroesJson[i])) and (not('\t' in HeroesJson[i])) and ('-' in HeroesJson[i])):
        if(not (HeroesJson[i] in BattletagList)):
            BattletagList.append(HeroesJson[i])

for i in range(len(T250Json)):
    if((not(' ' in T250Json[i])) and ('-' in T250Json[i])):
        Battletag = urllib.unquote(T250Json[i].encode('utf-8')).decode('utf-8')

        if(not (Battletag in BattletagList)):
            BattletagList.append(Battletag)


OutFile = open(sys.argv[5], 'w')
OutText = json.dumps(BattletagList)
OutFile.write(OutText)
OutFile.close()

