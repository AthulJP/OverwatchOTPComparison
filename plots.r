plots <- function(InFile, OutDir, HeroName, PlotVariance, Separate){
  
  PlayerData = fromJSON(InFile)
  
  Winrates = numeric()
  SkillRatings = numeric()
  
  for(count in 1:length(PlayerData)){
    Winrates[count] = PlayerData[[count]][[2]]
    SkillRatings[count] = PlayerData[[count]][[3]]
  }
  
  SkillRatings = sort(SkillRatings, index.return=TRUE)
  Winrates = Winrates[SkillRatings[[2]]]
  PlayerData = PlayerData[SkillRatings[[2]]]
  SkillRatings = SkillRatings[[1]]
  
  MeanSkillRatings = MeanWinrates = Variances = numeric()
  SRRanges = seq(RoundTo(min(SkillRatings), 50, floor), RoundTo(max(SkillRatings), 50, ceiling), 50)
  index = 1
  for(i in 2:(length(SRRanges))){
    SRsum = WRsum = numeric()
    while(index <= length(SkillRatings) & SkillRatings[index] <= SRRanges[i])
    {
      if(Separate){
        if(PlayerData[[index]][[4]] == "None"){
          WRsum = c(WRsum, Winrates[index])
          SRsum = c(SRsum, SkillRatings[index])
        }
      }else{
        WRsum = c(WRsum, Winrates[index])
        SRsum = c(SRsum, SkillRatings[index])
      }
      index = index + 1
    }
    if(length(SRsum) != 0){
      MeanSkillRatings = c(MeanSkillRatings, mean(SRsum))
      MeanWinrates = c(MeanWinrates, mean(WRsum))
      Variances = c(Variances, var(WRsum))
    }else{
      MeanSkillRatings = MeanWinrates = Variances = numeric()
    }
  }
  
  par(col="black")
  if(HeroName != "none"){
    png(paste(OutDir, "/", HeroName, ".png", sep=""), width=857, height=542)
  }else{
    png(paste(OutDir, "/WinrateVSSR.png", sep=""), width=857, height=542)
  }
  plot(SkillRatings, Winrates, pch='.', xlab="Skill Rating", ylab="Winrate")
  par(col="blue")
  lines(MeanSkillRatings, MeanWinrates, lwd=4)
  
  GraphTitle = LegendVec = ColorVec = PCharVec = character()
  LineTypeVec = LineWidthVec = numeric()
  if(HeroName != 'none'){
    for(count in 1:length(PlayerData)){
      if(PlayerData[[count]][[4]] == HeroName){
        par(col="red")
        points(PlayerData[[count]][[3]], PlayerData[[count]][[2]], pch="x")
        par(col="green")
        points(PlayerData[[count]][[3]], PlayerData[[count]][[5]], pch="o")
      }
    }
    GraphTitle = paste("Winrates for", capitalize(HeroName), "onetricks")
    LegendVec = c("Individual Winrate", "Mean Winrate", "Onetrick Player Winrate", paste("Onetricks Winrate on", capitalize(HeroName)))
    ColorVec = c("black", "blue", "red", "green")
    LineTypeVec = c(NA, 1, NA, NA)
    LineWidthVec = c(NA, 4, NA, NA)
    PCharVec = c('.', NA, 'x', 'o')
  }else{
    GraphTitle = "Winrate vs Skillrating"
    LegendVec = legend=c("Individual Winrate", "Mean Winrate")
    ColorVec = c("black", "blue")
    LineTypeVec = c(NA, 1)
    LineWidthVec = c(NA, 4)
    PCharVec = c('.', NA)
  }
  
  if(Separate){
    GraphTitle = paste(GraphTitle, "(Onetricks not included in mean winrate)")
  }
  if(PlotVariance){
    LegendVec = c(LegendVec, "Mean Winrate + Standard Deviation", "Mean Winrate - Standard Deviation")
    ColorVec = c(ColorVec, "purple", "purple")
    LineTypeVec = c(LineTypeVec, 1, 1)
    LineWidthVec = c(LineWidthVec, 2, 2)
    par(col="purple")
    lines(MeanSkillRatings, MeanWinrates + sqrt(Variances))
    lines(MeanSkillRatings, MeanWinrates - sqrt(Variances))
  }
    
  par(col="black")
  title(GraphTitle)
  legend(SkillRatings[1], 80, legend=LegendVec, col=ColorVec, lty=LineTypeVec, lwd=LineWidthVec, pch=PCharVec)
  
  
  dev.off()
}