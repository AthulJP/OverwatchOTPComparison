import json
import sys

if(len(sys.argv) != 3):
    print("Usage: python t100ob.py <input filename> <output filename>")
    sys.exit()

T100File = open(sys.argv[1], "r")
T100Json = json.load(T100File)
T100File.close()

BattletagList = []

for i in range(len(T100Json)):
    if(T100Json[i]['url']):
        BattletagList.append(T100Json[i]['url'][12:])

BattletagsFile = open(sys.argv[2], 'w')
BattletagsDump = json.dumps(BattletagList)
BattletagsFile.write(BattletagsDump)
BattletagsFile.close()
