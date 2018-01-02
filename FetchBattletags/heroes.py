import json
import sys

if(len(sys.argv) != 3):
    print("Usage: python heroes.py <input filename> <output filename>")
    sys.exit()

HeroesFile = open(sys.argv[1], "r")
HeroesJson = json.load(HeroesFile)
HeroesFile.close()


ListOfHeroes = [
    'doomfist',
    'genji',
    'mccree',
    'pharah',
    'reaper',
    'soldier76',
    'sombra',
    'tracer',
    'bastion',
    'hanzo',
    'junkrat',
    'mei',
    'torbjorn',
    'widowmaker',
    'dva',
    'orisa',
    'reinhardt',
    'roadhog',
    'winston',
    'zarya',
    'ana',
    'lucio',
    'mercy',
    'moira',
    'symmetra',
    'zenyatta'
]

BattletagList = []

for i in range(len(HeroesJson)):
    for j in range(len(ListOfHeroes)):
        if ((ListOfHeroes[j] in HeroesJson[i]) and HeroesJson[i][ListOfHeroes[j]]):
            BattletagList.append(HeroesJson[i][ListOfHeroes[j]][12:])
            break

BattletagsFile = open(sys.argv[2], 'w')
BattletagsDump = json.dumps(BattletagList)
BattletagsFile.write(BattletagsDump)
BattletagsFile.close()
