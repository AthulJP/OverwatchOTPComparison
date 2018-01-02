# Overwatch OTP Comparison

This works best on Linux systems, but it should work on Windows and Mac too (Except for the scripts, I think, IDK how Windows and Mac scripting works). I added some more features since I published the medium post.

Dependencies are:

R

Python

Pip

Scrapy

Hmisc, DescTools, RJsonIO (R packages)

How to use this:

Run the init script.

In order to get battletags of users to gather profiles of, you run battletags.sh or just run the individual spiders and then the scripts in the "FetchBattletags" directory in the same order as in the script. In order to run the MasterOverwatch spider, you need to download the full leaderboard webpage from MasterOverwatch and host it locally (I used simpleHTTPserver for this).

If you run GetCareerProfiles.py with the Battletags.json file, you will download the career profiles of the players whose battletags you just fetched. Before you do this however, you have to either run a local instance of OWAPI (https://github.com/SunDwarf/OWAPI, they have a guide on how to host an instance) or find a public instance which you can use and modify the URL in GetCareerProfiles.py to use that.

With PlayerStats.py you can extract certain stats from a players profile (Winrate, Skill Rating, etc.), filter players out based on time/games played, provide your own definition of what a onetrick is and label players as such.

With plots.r and automate.r, you can generate the graphs with the winrates, skill ratings and more.
