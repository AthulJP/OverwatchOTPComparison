ListOfHeroes = c('doomfist', 'genji', 'mccree', 'pharah', 'reaper', 'soldier76', 'sombra', 'tracer', 'bastion', 'hanzo', 'junkrat', 'mei', 'torbjorn', 'widowmaker', 'dva', 'orisa', 'reinhardt', 'roadhog', 'winston', 'zarya', 'ana', 'lucio', 'mercy', 'moira', 'symmetra', 'zenyatta')
source('plots.r')

for(HeroName in ListOfHeroes){
  plots("PlayerData.json", "Plots", HeroName, TRUE, TRUE)
}

plots("PlayerData.json", "Plots", "none", TRUE, TRUE)
