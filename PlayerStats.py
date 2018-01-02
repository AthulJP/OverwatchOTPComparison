import json
import argparse

ArgParser = argparse.ArgumentParser(description="Filter out information you aren't interested in from career profiles", epilog="Player must meet both time played and games played criteria")

ArgParser.add_argument("InFile", help="File containing all player profiles")
ArgParser.add_argument("OutFile", help="Output file")
ArgParser.add_argument("--time", help="Filter by minimum time (in hours) played (DEFAULT=15)", default=15, type=int)
ArgParser.add_argument("--games", help="Filter by minimum number of games played", default=0, type=int)
ArgParser.add_argument("--OTP", help="Definition of onetrick in percentage of time played (0-100)", default=75, type=int)


Arguments = ArgParser.parse_args()

ProfilesFile = open(Arguments.InFile, 'r')
ProfilesJson = json.load(ProfilesFile)
ProfilesFile.close()

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

Lists = []



for i in range(len(ProfilesJson)):
    PlayedEnough = False
    if(ProfilesJson[i][1] and
    ProfilesJson[i][1]['stats']['competitive'] and 
    ProfilesJson[i][1]['stats']['competitive']['overall_stats']['comprank'] and
    ProfilesJson[i][1]['stats']['competitive']['overall_stats']['games'] != 0 and
    ProfilesJson[i][1]['stats']['competitive']['game_stats']['time_played'] >= Arguments.time and
    ProfilesJson[i][1]['stats']['competitive']['game_stats']['games_played'] >= Arguments.games):
        Username = ProfilesJson[i][0]
        Winrate = ProfilesJson[i][1]['stats']['competitive']['overall_stats']['win_rate']

        SkillRating = ProfilesJson[i][1]['stats']['competitive']['overall_stats']['comprank']
        TimePlayed = ProfilesJson[i][1]['stats']['competitive']['game_stats']['time_played']
        HeroWinrate = 0
        OneTrick = False
        FirstHero = ''
        FirstHeroPlaytime = 0
        for j in range(len(ListOfHeroes)):
            FirstHero = ListOfHeroes[j]
            if(FirstHero in ProfilesJson[i][1]['heroes']['playtime']['competitive']):
                HeroPlaytime = ProfilesJson[i][1]['heroes']['playtime']['competitive'][FirstHero]
                
                if(FirstHeroPlaytime < HeroPlaytime):
                    FirstHeroPlaytime = HeroPlaytime
                if((HeroPlaytime/TimePlayed) > float(Arguments.OTP)/100):
                    OneTrick = True
                    HeroWinrate = ProfilesJson[i][1]['heroes']['stats']['competitive'][FirstHero]['general_stats']['win_percentage'] * 100
                    #if(HeroWinrate < Winrate): #Just something I used to check how many onetricks had higher average winrates than on their main hero
                    #    print("{} : Winrate = {}, {} Winrate = {}".format(Username.encode('utf-8'), Winrate, FirstHero, HeroWinrate))
                    break

        if(not OneTrick):
            FirstHero = 'None'
        
        Lists.append([Username, Winrate, SkillRating, FirstHero, HeroWinrate, FirstHeroPlaytime])


Outfile = open(Arguments.OutFile, 'w')
Outfile.write(json.dumps(Lists))
Outfile.close()
