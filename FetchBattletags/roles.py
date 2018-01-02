import json
import sys

if(len(sys.argv) != 3):
    print("Usage: python roles.py <input filename> <output filename>")
    sys.exit()

RolesFile = open(sys.argv[1], "r")
RolesJson = json.load(RolesFile)
RolesFile.close()


ListOfRoles = [
    'off',
    'def',
    'tan',
    'sup'
]

BattletagList = []

for i in range(len(RolesJson)):
    for j in range(len(ListOfRoles)):
        if ((ListOfRoles[j] in RolesJson[i]) and RolesJson[i][ListOfRoles[j]]):
            BattletagList.append(RolesJson[i][ListOfRoles[j]][12:])
            break

BattletagsFile = open(sys.argv[2], 'w')
BattletagsDump = json.dumps(BattletagList)
BattletagsFile.write(BattletagsDump)
BattletagsFile.close()
