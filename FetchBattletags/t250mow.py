import json
import sys

if(len(sys.argv) != 3):
    print("Usage: python heroes.py <input filename> <output filename>")
    sys.exit()

T250File = open(sys.argv[1], "r")
T250Json = json.load(T250File)
T250File.close()

BattletagList = []

for i in range(len(T250Json)):
    if(T250Json[i]['url']):
        BattletagList.append(T250Json[i]['url'][46:])

BattletagsFile = open(sys.argv[2], 'w')
BattletagsDump = json.dumps(BattletagList)
BattletagsFile.write(BattletagsDump)
BattletagsFile.close()
